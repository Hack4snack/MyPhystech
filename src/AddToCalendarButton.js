import React, { useState, useEffect, useRef } from 'react';
import { StyleSheet, Text, View, Image, TextInput, Animated } from 'react-native';
import styled from 'styled-components/native';
import IconF from "react-native-vector-icons/Feather";
import {Badge} from "react-native-elements";

export default function AddToCalendarButton({added, setAdded}) {
  const [ coords, setCoords ] = useState({ x: 0, y: 0 });
  //const badgeAnim = useRef(new Animated.ValueXY({ x: 0, y: 0 })).current;
  const addAnim = useRef(new Animated.Value(1)).current;
  const badgeRef = useRef();
  const firstUpdate = useRef(true);

  const BadgeWrapper = styled.View`
    background: ${added ? "#FF5045" : "#fff"};
    border-radius: 50px;
    padding: 2px;
  `;

  useEffect(() => {
    if(firstUpdate.current) {
      firstUpdate.current = false;
      addAnim.setValue(1);
      return;
    }
    addAnim.setValue(0);
    Animated.spring(
      addAnim,
      {
        toValue: 1,
        useNativeDriver: true
      }
    ).start();
  }, [added]);


  return (
    <View>

        <IconF name="calendar" size={25} color={"#fff"} onPress={() => setAdded(!added)} />
        <Animated.View
          style={{ transform: [{scale: addAnim}] }}
        >
        <Badge
          Component={() => <BadgeWrapper><IconF name={added ? "check" : "plus"} size={12} color={added ? "#fff" : "#000"} /></BadgeWrapper>}
          onPress={() => setAdded(!added)}
          containerStyle={{ position: 'absolute', bottom: 10, right: -6 }}
          badgeStyle={{
            backgroundColor: added ? "#FF5045" : "#fff",
            borderWidth: 0, // Remove Border
            shadowColor: 'rgba(0,0,0, 0.0)', // Remove Shadow IOS
            shadowOffset: { height: 0, width: 0 },
            shadowOpacity: 0,
            shadowRadius: 0,
            elevation: 0 // This is for Android
          }}
          textStyle={{ color: '#1E2631' }}
        />
      </Animated.View>
    </View>
  );
}