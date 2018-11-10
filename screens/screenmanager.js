import React from 'react';
import { StyleSheet, Text, View ,Button} from 'react-native';
import { createStackNavigator } from 'react-navigation';
import MainScreen from './mainscreen';
import Screen1 from './screen1';
import Screen2 from './screen2';

const Screens = createStackNavigator({
    MainScreen: { screen: MainScreen },
    Screen1: { screen: Screen1 },
    Screen2: { screen: Screen2 },
});

export default Screens;
