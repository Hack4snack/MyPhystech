import React, { useState, useEffect } from 'react';
import {StyleSheet, Text, View, Image, Button, StatusBar, TouchableOpacity} from 'react-native';
import styled from 'styled-components/native';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';
import {signIn} from "../actions";
import Logo from './Logo';
import {background, active1} from '../assets/palettes/dark';

function TopicsSuggest({signIn, user, navigation}) {
  return (
    <Wrapper>
      <StatusBar barStyle="light-content" backgroundColor={background} />
      <Logo style={{margin: 20}} />
      <TextInputStyled placeholder={'Поиск'} />
      <Text style={{color: 'white'}}>Choose a topics pls</Text>
      <Continue onPress={() => navigation.navigate('Home')}>
        <Text style={{color: 'white'}}>Продолжить</Text>
      </Continue>
    </Wrapper>
  );
}

const mapStateToProps = state => ({
  user: state.user
});

const mapDispatchToProps = dispatch => bindActionCreators({signIn}, dispatch);

export default connect(mapStateToProps, mapDispatchToProps)(TopicsSuggest);

const Wrapper = styled.View`
  flex: 1;
  align-items: center;
  justify-content: flex-start;
  background-color: ${background};
`;

const TextInputStyled = styled.TextInput`
  align-self: stretch;
  background-color: #2B3543;
  margin-left: 25px;
  margin-right: 15px;
  margin-bottom: 15px;
  padding-left: 15px;
  padding-right: 15px;
  font-size: 14px;
  border-radius: 50px;
  height: 40px;
  color: white;
`;

const Continue = styled.TouchableOpacity`
  position: absolute;
  bottom: 30px;
  text-align: center;
  font-size: 20px;
  background-color: ${active1};
  padding: 10px;
  border-radius: 50px;
`;