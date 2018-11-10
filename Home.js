import React from 'react';
import { StyleSheet, Text, View ,Button} from 'react-native';
import { createStackNavigator } from 'react-navigation';

class Home extends React.Component {
    render() {
      return (
        <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
          <Text>Details Screen</Text>
          <Button
            title="Go to Details... again"
            onPress={() => this.props.navigation.push('Page2')}
          />
          <Button
            title="Go to Home"
            onPress={() => this.props.navigation.navigate('Page1')}
          />
          <Button
            title="Go back"
            onPress={() => this.props.navigation.goBack()}
          />
        </View>
      );
    }
  }
  