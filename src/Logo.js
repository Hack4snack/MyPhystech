import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, Image, TextInput, FlatList, SafeAreaView, StatusBar } from 'react-native';
import styled from 'styled-components/native';
import { loadAsync } from 'expo-font';

export default function Logo(props) {
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

  return (<Wrapper {...props}>My Phystech</Wrapper>);
}

const Wrapper = styled.Text`
  color: #FF5045;
  font-size: 20px;
  font-weight: bold;
  font-family: 'Montserrat';
`;