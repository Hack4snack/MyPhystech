import React, { useState, useEffect } from 'react';
import {StyleSheet, Text, View, Image, Button, StatusBar} from 'react-native';
import styled from 'styled-components/native';
import * as Google from 'expo-google-app-auth';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';
import {signIn} from "../actions";
import Logo from './Logo';
import {background, active1} from '../assets/palettes/dark';

function Login({signIn, user, navigation}) {
  async function logInAsync() {
    try {
      const { type, accessToken, user, idToken } = await Google.logInAsync({
        androidClientId: '942480069892-05kgachoktolijpd718lpna2smq6rsdk.apps.googleusercontent.com',
      });
      signIn({idToken});
      if (type === 'success') {
        // Then you can use the Google REST API
        let userInfoResponse = await fetch('https://www.googleapis.com/userinfo/v2/me', {
          headers: { Authorization: `Bearer ${accessToken}` },
        });
        console.log('user: ', user.name);
      }
    } catch {

    }
  }

  if(user.info?.firstTime) {
    navigation.navigate('GroupSuggest');
  }

  if(user.info && !user.info.firstTime) {
    navigation.navigate('Home');
  }

  return (
    <Wrapper>
      <StatusBar barStyle="light-content" backgroundColor={background} />
      <Logo style={{margin: 20}} />
      <Button
        disabled={false}
        color={active1}
        title="Войти с почты @phystech.edu"
        onPress={() => {
          logInAsync();
        }}
      />
      {user.isLoading ? <Text style={{color: 'white'}}>Loading...</Text> : null}
    </Wrapper>
  );
}

const mapStateToProps = state => ({
  user: state.user
});

const mapDispatchToProps = dispatch => bindActionCreators({signIn}, dispatch);

export default connect(mapStateToProps, mapDispatchToProps)(Login);

const Wrapper = styled.View`
  flex: 1;
  height: 500px;
  justify-content: flex-start;
  align-items: center;
  background-color: ${background};
`;

