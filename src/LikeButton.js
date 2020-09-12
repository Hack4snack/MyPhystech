import React, { useState, useEffect, useRef } from 'react';
import { StyleSheet, Text, View, Image, TextInput, Animated } from 'react-native';
import styled from 'styled-components/native';
import IconAnt from 'react-native-vector-icons/AntDesign';

export default function LikeButton({liked, setLiked}) {
  const likeAnim = useRef(new Animated.Value(0)).current;
  const firstUpdate = useRef(true);

  useEffect(() => {
    if(firstUpdate.current) {
      firstUpdate.current = false;
      likeAnim.setValue(1);
      return;
    }
    likeAnim.setValue(0);
    Animated.spring(
      likeAnim,
      {
        toValue: 1,
        useNativeDriver: true
      }
    ).start();
  }, [liked]);


  return (
    <View style={{ flexDirection: 'row', alignItems: 'center' }}>
      <Animated.View style={{ transform: [{scale: likeAnim}] }}>
      {liked ?
        <IconAnt name="heart" size={25} color="#FF5045" onPress={() => setLiked(false)} />
        :
        <IconAnt name="hearto" size={25} color="#fff" onPress={() => setLiked(true)} />
      }
      </Animated.View>
      <LikedAmount>12</LikedAmount>
    </View>
  );
}

const LikedAmount = styled.Text`
  color: white;
  font-weight: bold;
  margin-left: 8px;
  position: relative;
  bottom: 1px;
`;