import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, Image, TextInput, FlatList, SafeAreaView } from 'react-native';
import styled from 'styled-components/native';
import { loadAsync } from 'expo-font';
import Dash from 'react-native-dash';
import Menu from './Menu';
import Event from './Event';


export default function Feed() {
  const [loaded, setLoaded] = useState(false);

  async function _loadAssetsAsync() {
    await loadAsync({
      'Montserrat': require("../assets/fonts/Montserrat-Italic.ttf"),
    });
    setLoaded(true);
  }

  useEffect(() => {
    _loadAssetsAsync();
  }, []);

  if (!loaded) {
    return null;
  }

  return (
    <Wrapper>
      <TopLine>
        <Menu />
        <Logo>My Phystech</Logo>
      </TopLine>
      <TextInputStyled placeholder={'Поиск'} />
      <SafeAreaViewStyled>
      <FlatList
        data={[{id: 1}, {id: 2}, {id: 3}]}
        renderItem={Event}
        keyExtractor={item => item.id}
        ItemSeparatorComponent={() => <Dash dashColor={'#2B3543'} style={{height: 1}} />}
      />
      </SafeAreaViewStyled>
    </Wrapper>
  );
}

const Wrapper = styled.View`
  padding-top: 20px;
  width: 100%;
  height: 100%;
  background: #161F2A;
`;

const SafeAreaViewStyled = styled.SafeAreaView`
  flex: 1;
`;

const TextInputStyled = styled.TextInput`
  background: #2B3543;
  margin-left: 15px;
  margin-right: 15px;
  margin-bottom: 15px;
  padding-left: 15px;
  padding-right: 15px;
  font-size: 14px;
  border-radius: 50px;
  height: 40px;
  color: white;
`;

const TopLine = styled.View`
  flex-direction: row;
  align-items: center;
`;

const Logo = styled.Text`
  color: #FF5045;
  font-size: 20px;
  font-weight: bold;
  font-family: 'Montserrat';
`;