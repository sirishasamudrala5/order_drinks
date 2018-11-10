import React from 'react';
import { StyleSheet, Text, View ,Button,TouchableOpacity,} from 'react-native';

export default class MainScreen extends React.Component {
    static navigationOptions = {
        title: 'Gala',
    };
  render() {
    const { navigate } = this.props.navigation
    return (

      <View style={styles.container}>
        <Text style={styles.titleText}>Gala</Text>
        <Text>Party at Home!</Text>
        <TouchableOpacity onPress={() => navigate('Screen1')}>
            <Text>Lets Go to page 1!</Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={() => navigate('Screen2')}>
            <Text>Lets Go to page 2!</Text>
        </TouchableOpacity>
        {/* <Button onPress={() => navigate('Page2')} title="Let's Go!" color="#841584" accessibilityLabel="Learn more about this purple button" /> */}
      </View>     
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fafafa',
    alignItems: 'center',
    justifyContent: 'center'
  },
  titleText: {
    fontSize: 40,
    fontWeight: 'bold',
  },
});