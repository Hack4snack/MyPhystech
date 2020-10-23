import './wdyr';
import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, Image, TextInput, Button } from 'react-native';
import styled from 'styled-components/native';
import { loadAsync } from 'expo-font';
import axios from 'axios';
import axiosMiddleware from 'redux-axios-middleware';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import reducer from './reducers';
import Navigator from "./src/Navigator";


const client = axios.create({
  baseURL:`http://rishel.pythonanywhere.com/`,
  responseType: 'json'
});

const store = createStore(reducer, applyMiddleware(thunk, axiosMiddleware(client, { returnRejectedPromiseOnError: true })));

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
    <Provider store={store}>
      <Navigator />
    </Provider>
  );
}