import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, Image } from 'react-native';
import styled from 'styled-components/native';

export default function Menu() {
  return (
    <Wrapper>
      <StyledView1 />
      <StyledView2 />
      <StyledView3 />
    </Wrapper>
  );
}

const Wrapper = styled.View`
  margin: 15px;
`;

const StyledView1 = styled.View`
  width: 10px;
  height: 3px;
  margin-bottom: 4px;
  background: white;
  border-radius: 50px;
`;

const StyledView2 = styled.View`
  width: 20px;
  height: 3px;
  margin-bottom: 4px;
  background: white;
  border-radius: 50px;
`;

const StyledView3 = styled.View`
  width: 15px;
  height: 3px;
  background: white;
  border-radius: 50px;
`;