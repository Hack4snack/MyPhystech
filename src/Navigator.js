import React from "react";
import {NavigationContainer} from "@react-navigation/native";
import IconF from "react-native-vector-icons/Feather";
import Ionicons from "react-native-vector-icons/Ionicons";
import {connect} from 'react-redux';
import PublicFeed from "./PublicFeed";
import PersonalFeed from './PersonalFeed';
import Schedule from "./Schedule";
import Login from "./Login";
import GroupSuggest from './GroupSuggest';
import TopicsSuggest from './TopicsSuggest';
import {createBottomTabNavigator} from "@react-navigation/bottom-tabs";
import { createStackNavigator } from '@react-navigation/stack';

const Tab = createBottomTabNavigator();
const Stack = createStackNavigator();

function Navigator({user}) {
  return <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Login" component={Login} options={{headerShown: false}} />
        <Stack.Screen name="GroupSuggest" component={GroupSuggest} options={{headerShown: false}} />
        <Stack.Screen name="TopicsSuggest" component={TopicsSuggest} options={{headerShown: false}} />
        <Stack.Screen options={{headerShown: false}} name="Home" component={() =>
          <Tab.Navigator
            lazy={false}
            screenOptions={({route}) => ({
              tabBarIcon: ({focused, color, size}) => {
                let iconName;

                switch (route.name) {
                  case 'PersonalFeed':
                    iconName = 'ios-home';
                    break;
                  case 'PublicFeed':
                    iconName = 'ios-search';
                    break;
                  case 'Schedule':
                    iconName = focused ? 'calendar' : 'calendar';
                    return <IconF name={iconName} size={25} color={color}/>;
                    break;
                  case 'Profile':
                    iconName = 'ios-person';
                }

                // You can return any component that you like here!
                return <Ionicons name={iconName} size={size} color={color}/>;
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
            <Tab.Screen name="PersonalFeed" component={PersonalFeed} options={{title: 'Рекомендации'}}/>
            <Tab.Screen name="PublicFeed" component={PublicFeed} options={{title: 'Поиск'}}/>
            <Tab.Screen name="Schedule" component={Schedule} options={{title: 'Расписание'}}/>
            <Tab.Screen name="Profile" component={Schedule} options={{title: 'Профиль'}}/>
          </Tab.Navigator>
        } />
      </Stack.Navigator>
    </NavigationContainer>;
}

const mapStateToProps = state => ({
  user: state.user
});

export default connect(mapStateToProps)(Navigator);