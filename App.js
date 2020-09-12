import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, Image, TextInput } from 'react-native';
import styled from 'styled-components/native';
import { loadAsync } from 'expo-font';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Ionicons from 'react-native-vector-icons/Ionicons';
import IconF from "react-native-vector-icons/Feather";
import Feed from './src/Feed';
import Schedule from './src/Schedule';

const Tab = createBottomTabNavigator();

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
    <NavigationContainer>
      <Tab.Navigator
        screenOptions={({ route }) => ({
          tabBarIcon: ({ focused, color, size }) => {
            let iconName;

            switch(route.name) {
              case 'Feed':
                iconName = 'ios-home';
                break;
              case 'Schedule':
                iconName = focused ? 'calendar' : 'calendar';
                return <IconF name={iconName} size={25} color={color} />
                break;
              case 'Profile':
                iconName = 'ios-person';
            }

            // You can return any component that you like here!
            return <Ionicons name={iconName} size={size} color={color} />;
          },
        })}
        tabBarOptions={{
          tabStyle: {
            justifyContent: 'center',
          },
          style: {
            backgroundColor: '#1E2631',
            borderTopWidth: 0,
            borderTopColor: '#1E2631',
            outline: 'none',
          },
          showLabel: false,
          activeTintColor: '#FF5045',
          inactiveTintColor: '#fff'
        }}
      >
        <Tab.Screen name="Feed" component={Feed} options={{title: 'Лента'}} />
        <Tab.Screen name="Schedule" component={Schedule} options={{title: 'Расписание'}} />
        <Tab.Screen name="Profile" component={Schedule} options={{title: 'Профиль'}} />
      </Tab.Navigator>
    </NavigationContainer>
  );
}