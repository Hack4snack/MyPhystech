import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, Image, TextInput } from 'react-native';
import styled from 'styled-components/native';
import IconAnt from 'react-native-vector-icons/AntDesign';
import IconF from 'react-native-vector-icons/Feather';
import { Badge } from 'react-native-elements';
import moment from 'moment';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import { addToSchedule } from "../actions";
import LikeButton from "./LikeButton";
import AddToCalendarButton from "./AddToCalendarButton";

const maxLimit = 88;

function Event({item, addToSchedule}) {
  const [ expanded, setExpanded ] = useState(false);
  const [ liked, setLiked ] = useState(false);
  const [ added, setAdded ] = useState(false);
  const fullText = item.description;

  useEffect(() => {
    if(added) {
      addToSchedule({id: item.id});
      console.debug('123123');
    }
  }, [added]);

  return (
    <Wrapper>
      <UpperLine>
        <Public>
          <PublicAvatar source={{uri: item.group_img_url}}></PublicAvatar>
          <PublicTitle>{item.public_name}</PublicTitle>
        </Public>
        <PublicationDate>{moment(item.publication_time).fromNow()}</PublicationDate>
      </UpperLine>
      <Preview source={{uri: item.event_img_url}}></Preview>
      <View style={{flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center'}}>
        <LikeButton liked={liked} setLiked={setLiked} />
        <AddToCalendarButton added={added} setAdded={setAdded} />
      </View>
      <Title>
        {item.title}
      </Title>
      <Info>
        <TagsWrapper>
          {item.tags.map(t => <Tag key={t}>{t}</Tag>)}
        </TagsWrapper>
        <Time>{moment(item.start_time).format('DD.MM.YYYY HH:mm')}</Time>
      </Info>
      <FullText>
        {fullText.length > maxLimit && !expanded ?
          <Text>{fullText.substring(0, maxLimit-3)}<More onPress={() => setExpanded(true)}>...еще</More></Text> :
          <Text>{fullText}</Text> }
      </FullText>
    </Wrapper>
  );
}

const mapDispatchToProps = dispatch => bindActionCreators({addToSchedule}, dispatch);

export default connect(null, mapDispatchToProps)(Event);

const Wrapper = styled.View`
  width: 100%;
  background: #1E2631;
  padding: 15px;
`;

const UpperLine = styled.View`
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
`;

const Public = styled.View`
  flex: 1;
  flex-direction: row;
  align-items: center;
`;

const PublicAvatar = styled.Image`
  width: 30px;
  height: 30px;
  border-radius: 50px;
  margin-right: 10px;
`;

const PublicTitle = styled.Text`
  color: white;
  font-family: Roboto;
  font-weight: 600;
`;

const PublicationDate = styled.Text`
  color: #5A677F;
  font-family: Roboto;
  font-weight: 600;
`;

const Preview = styled.Image`
  width: 100%;
  height: 200px;
  border-radius: 15px;
  margin-bottom: 10px;
`;

const Tag = styled.Text`
  color: #FF5045;
  font-weight: bold;
  margin-right: 5px;
`;

const Time = styled.Text`
  color: #5A677F
`;

const Title = styled.Text`
  color: white;
  font-family: Montserrat;
  font-size: 20px;
  font-weight: bold;
  margin-top: 0px;
`;

const FullText = styled.Text`
  color: white;
  font-size: 13px;
`;

const More = styled.Text`
  color: #c1c1c1;
`;

const Info = styled.View`
  flex-direction: row;
  justify-content: space-between;
  margin-bottom: 3px;
  margin-top: 3px;
`;

const TagsWrapper = styled.View`
  flex-flow: row;
`;