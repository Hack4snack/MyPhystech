import React, { useState, useEffect } from 'react';
import {StyleSheet, Text, View, Image, Button, StatusBar, FlatList, ImageBackground, TouchableWithoutFeedback} from 'react-native';
import styled from 'styled-components/native';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';
import {signIn, fetchStudyChannels} from "../actions";
import Logo from './Logo';
import {background, active1} from '../assets/palettes/dark';
import { LinearGradient } from 'expo-linear-gradient';
import Checkmark from './Checkmark';

function RenderCard({item, style, checkedChannels, setCheckedChannels, initialChecked}) {
  const [checked, setChecked] = useState(initialChecked);

  function toggleCheck() {
    if(!checked) {
      setChecked(true);
      setCheckedChannels([item.id]);

    } else {
      setChecked(false);
      setCheckedChannels(checkedChannels.filter(c => c !== item.id));
    }
  }

  return (
    <Card
      source={{uri: `https://picsum.photos/200?title=${item.title}`}}
      imageStyle={{
        borderRadius: 10
      }}
      style={style}
    >
        <TouchableWithoutFeedback
          style={{flex: 1, width: '100%'}}
          onPress={() => {
            toggleCheck();
          }}
        >
        <LinearGradientStyled
          colors={['transparent', 'rgba(0,0,0,0.8)']}>
          <Checkmark {...{checked: initialChecked}} style={{alignSelf: 'flex-start', margin: 5}} />
          <Text style={{color: 'white'}}>{item.title}</Text>
        </LinearGradientStyled>
      </TouchableWithoutFeedback>
    </Card>
  );
}

function GroupSuggest({signIn, user, channels, navigation, fetchStudyChannels}) {
  const separatorWidth = 10;
  const [text, setText] = useState('');
  const [channelsObj, setChannelsObj] = useState(channels.list.reduce((acc, val) => ({...acc, [val.id]: {...val, checked: false}}), {}));
  const [checkedChannels, setCheckedChannels] = useState([]);

  useEffect(() => {
    fetchStudyChannels({limit: 20, offset: 0, text: ''});
  }, []);

  useEffect(() => {
    fetchStudyChannels({limit: 20, offset: 0, text});
    console.log(text);
  }, [text]);

  useEffect(() => {
    console.log(checkedChannels);
  }, [checkedChannels]);

  return (
    <Wrapper>
      <StatusBar barStyle="light-content" backgroundColor={background} />
      <Logo style={{margin: 20}} />
      <TextInputStyled value={text} onChangeText={setText} placeholder={'Поиск'} />
      <Hint>Выберите свою учебную группу</Hint>
      <SafeAreaViewStyled>
        <FlatListStyled
          data={channels.list}
          renderItem={({item, index}) =>
            <RenderCard {...{item, checkedChannels, setCheckedChannels, initialChecked: checkedChannels.some(c => c === item.id)}} style={{marginLeft: index % 3 !== 0 ? separatorWidth : 0}} />
          }
          keyExtractor={item => String(item.title)}
          numColumns={3}
          columnWrapperStyle={{
            justifyContent: 'center',
          }}
          ItemSeparatorComponent={
            () => <View style={{ height: separatorWidth }}/>
          }
        />
      </SafeAreaViewStyled>
      <BackgroundBottom
        colors={['transparent', 'rgba(0,0,0,0.8)']} >
        <Skip onPress={() => navigation.navigate('TopicsSuggest')}>
          {checkedChannels.length === 0 ? 'Пропустить >' : 'Продолжить >'}
        </Skip>
      </BackgroundBottom>
    </Wrapper>
  );
}

const mapStateToProps = state => ({
  user: state.user,
  channels: state.channels
});

const mapDispatchToProps = dispatch => bindActionCreators({signIn, fetchStudyChannels}, dispatch);

export default connect(mapStateToProps, mapDispatchToProps)(GroupSuggest);

const Wrapper = styled.View`
  flex: 1;
  justify-content: flex-start;
  align-items: center;
  background-color: ${background};
`;

const Hint = styled.Text`
  align-self: flex-start;
  color: #909090;
  margin-top: 5px;
  margin-bottom: 10px;
  margin-left: 15px;
`;

const BackgroundBottom = styled(LinearGradient)`
  position: absolute;
  bottom: 0;
  width: 100%;
  align-items: center;
`;

const Skip = styled.Text`
  margin-bottom: 20px;
  margin-top: 20px;
  color: white;
  font-size: 20px;
`;

const TextInputStyled = styled.TextInput`
  align-self: stretch;
  background: #2B3543;
  margin-left: 15px;
  margin-right: 15px;
  padding-left: 15px;
  padding-right: 15px;
  font-size: 14px;
  border-radius: 50px;
  height: 40px;
  color: white;
`;

const SafeAreaViewStyled = styled.SafeAreaView`
  align-self: stretch;
  flex: 1;
`;

const FlatListStyled = styled.FlatList`
  margin-left: 15px;
  margin-right: 15px;
`;

const Card = styled.ImageBackground`
  flex: 1;
  height: 100px;
  width: 80px;
  background-color: ${active1};
  border-radius: 10px;
  justify-content: flex-end;
  align-items: center;
  
  &:nth-child(3n+1) {
    margin-left: 0;
  }
  
  &:last-child {
    margin-right: 100px;
  }
`;

const LinearGradientStyled = styled(LinearGradient)`
  flex: 1;
  width: 100%;
  justify-content: space-between;
  align-items: center;
  padding: 5px;
  border-radius: 10px;
`;