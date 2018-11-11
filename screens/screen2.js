import React from 'react';
import { AppRegistry, StyleSheet, ActivityIndicator, ListView, Text, View, Alert,Image, Platform, Button, TouchableHighlight} from 'react-native';

url = '<server ip>'

export default class screen2 extends React.Component {
    static navigationOptions = {
        title: 'Drinks',
    };
    constructor(props) {
      super(props);
      this.state = {
        isLoading: true
      }
    }
  
    GetItem (pname,pquantity,pcost) {
      Alert.alert(pname + " " + pquantity +  " " + pcost);     
    }

    componentDidMount() {
      return fetch(url+'/ListProducts',{method:'POST'})
      .then((response) => response.json())
      .then((responseJson) => {
        let ds = new ListView.DataSource({rowHasChanged: (r1, r2) => r1 !== r2});
        this.setState({
          isLoading: false,
          dataSource: ds.cloneWithRows(responseJson),
        }, function() {
          // In this block you can do something with new state.
        });
      })
      .catch((error) => {
        console.error(error);
      });
    
    }

    ListViewItemSeparator = () => {
      return (
        <View
          style={{
            height: .5,
            width: "100%",
            backgroundColor: "#fafafa",
          }}
        />
      );
    }

    render(){
      if (this.state.isLoading) {
        return (
          <View style={{flex: 1, paddingTop: 20,backgroundColor: "#fafafa"}}>
            <ActivityIndicator />
          </View>
        );
      }
      return (   
        <View style={styles.MainContainer}>
          <ListView
            dataSource={this.state.dataSource}
            renderSeparator= {this.ListViewItemSeparator}
            renderRow={(rowData) =>
            <View style={{flex:1, flexDirection: 'row'}}>
              <Image source = {{ uri: rowData.pimage }} style={styles.imageViewContainer} />
              <View style={styles.textContainer}>
                
                <Text style={{ fontSize: 20,textAlign:'justify'}}>{rowData.pname}</Text>
                <Text style={{ fontSize: 14, textAlign:'justify'}}>{rowData.pdescription},{rowData.pdescription},{rowData.pdescription},{rowData.pquantity}</Text>
                <View style={{flexDirection: 'row' }}>
                <View style={{flex:1}}>
                  <Text style={{ fontSize: 14,justifyContent: 'flex-start',}}>{rowData.pdescription}</Text>
                  </View>
                <View style={{flex:1, backgroundColor:'#ffa800',borderRadius:5}}>
                <TouchableHighlight onPress={this.GetItem.bind(this, rowData.pdescription,rowData.pquantity,rowData.pcost)} style={{ justifyContent: 'flex-end'}}>
                    <Text style={{fontSize: 14, height:25, maxWidth:20, textAlignVertical:'center'}}>Add</Text>
                </TouchableHighlight>
                  {/* <Button containerStyle={{padding:10, height:45, overflow:'hidden', borderRadius:4, backgroundColor: 'white'}}disabledContainerStyle={{backgroundColor: 'grey'}} style={{fontSize: 20, color: 'green'}} onPress={this.GetItem.bind(this, rowData.pdescription,rowData.pquantity,rowData.pcost)} title="Add"/>  */}
                  </View>
                </View>
                
              </View>
            </View>

        }
        />
      </View>
      );
    }
}

const styles = StyleSheet.create({
  titleText: {
    fontSize: 40,
    fontWeight: 'bold',
  },
  MainContainer :{
    // Setting up View inside content in Vertically center.
    flex:1,
    margin: 10,
    backgroundColor: '#fafafa',
    alignItems: 'center',
    justifyContent: 'center'   
  },
  imageViewContainer: {
    width: '30%',
    height: 100 ,
    margin: 10,
    borderRadius : 10
     
    },
    textContainer: {
      width: '70%',
      height: 100 ,
      margin:10       
    }
});

AppRegistry.registerComponent('screen2', () => screen2);

