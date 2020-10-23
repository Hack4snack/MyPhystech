import React, { useState, useEffect, useRef } from 'react';
import { StyleSheet, Text, View, Image, TextInput, Animated, TouchableWithoutFeedback } from 'react-native';
import styled from 'styled-components/native';
import IconAnt from 'react-native-vector-icons/Ionicons';

export default function Checkmark({checked, onChange, style}) {
  const checkAnim = useRef(new Animated.Value(0)).current;
  const firstUpdate = useRef(true);

  useEffect(() => {
    if(firstUpdate.current) {
      firstUpdate.current = false;
      checkAnim.setValue(checked ? 1 : 0);
      return;
    }
    if(checked) {
      checkAnim.setValue(0);
      Animated.spring(
        checkAnim,
        {
          toValue: 1,
          useNativeDriver: true
        }
      ).start();
    } else {
      Animated.timing(
        checkAnim,
        {
          toValue: 0,
          duration: 200,
          useNativeDriver: true
        }
      ).start();
    }

  }, [checked]);

  return (
    <Wrapper style={style} >
      <TouchableWithoutFeedback onPress={() => onChange?.(false)}>
        <Animated.View style={{ transform: [{scale: checkAnim}],  }}>
          {(<IconAnt name="ios-checkmark-circle" size={25} color="#FF5045" />)
          }
        </Animated.View>
      </TouchableWithoutFeedback>
    </Wrapper>
  );
}

const Circle = styled.View`
  width: 40px;
  height: 40px;
  border-radius: 50px;
  border: 2px solid black;
`;

const Wrapper = styled.View`
  flex-direction: row;
  align-items: center;
  background-color: white;
  border-radius: 50px;
  width: 20px;
  height: 20px;
  align-self: flex-start;
`;