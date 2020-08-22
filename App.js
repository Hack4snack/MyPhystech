import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, Image, TextInput } from 'react-native';
import styled from 'styled-components/native';
import { loadAsync } from 'expo-font';
import Feed from './src/Feed';

export default function App() {
  const [loaded, setLoaded] = useState(false);

  async function _loadAssetsAsync() {
    await loadAsync({
      Montserrat: require("./assets/fonts/Montserrat-Italic.ttf"),
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
    <Feed />
  );
}