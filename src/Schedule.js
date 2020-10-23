import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, Image, TextInput } from 'react-native';
import { Agenda } from 'react-native-calendars';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import moment from 'moment';
import styled from 'styled-components/native';
import { fetchSchedule } from '../actions';

function Schedule({schedule, fetchSchedule}) {
  const items = schedule.reduce((acc, val) => ({
      ...acc,
      [moment(val.start_time).format('YYYY-MM-DD')]: acc[moment(val.start_time).format('YYYY-MM-DD')] ?
        [val].concat(acc[moment(val.start_time).format('YYYY-MM-DD')]) : [val]
    })
    , {});
  console.debug(schedule[schedule.length-1]);


  useEffect(() => {
    fetchSchedule({});
  }, []);

  return (
    <Wrapper>
      <SafeAreaViewStyled>
        <Agenda
          // The list of items that have to be displayed in agenda. If you want to render item as empty date
          // the value of date key has to be an empty array []. If there exists no value for date key it is
          // considered that the date in question is not yet loaded
          items={items}
          // Callback that gets called when items for a certain month should be loaded (month became visible)
          loadItemsForMonth={(month) => {console.log('trigger items loading')}}
          // Callback that fires when the calendar is opened or closed
          onCalendarToggled={(calendarOpened) => {console.log(calendarOpened)}}
          // Callback that gets called on day press
          onDayPress={(day)=>{
            fetchSchedule({});
          }}
          // Callback that gets called when day changes while scrolling agenda list
          onDayChange={(day)=>{

          }}
          // Initially selected day
          selected={moment().format('YYYY-MM-DD')}
          // Max amount of months allowed to scroll to the past. Default = 50
          pastScrollRange={50}
          // Max amount of months allowed to scroll to the future. Default = 50
          futureScrollRange={50}
          renderItem={(item, firstItemInDay) =>
            <ItemWrapper>
              {firstItemInDay ? <Divider/> : null}
              <Item style={{marginTop: firstItemInDay ? 10 : 0}}>
                <Title numberOfLines={1}>{item.title}</Title>
                <Time>{`${moment(item.start_time).format('HH:mm')}${item.end_time ? `- ${moment(item.end_time).format('HH:mm')}` : ''}`}</Time>
              </Item>
            </ItemWrapper>
          }
          renderEmptyData = {() => <NoEvents><Text>Событий на этот день нет.</Text></NoEvents>}
        />
      </SafeAreaViewStyled>
    </Wrapper>
  );
}

const mapStateToProps = state => ({
  schedule: state.schedule.list
});

const mapDispatchToProps = dispatch => bindActionCreators({fetchSchedule}, dispatch);

export default connect(mapStateToProps, mapDispatchToProps)(Schedule);

const Wrapper = styled.View`
  padding-top: 10px;
  width: 100%;
  height: 100%;
  background: #161F2A;
`;

const SafeAreaViewStyled = styled.SafeAreaView`
  flex: 1;
`;

const ItemWrapper = styled.View`
  width: 100%;
  margin-bottom: 10px;
`;

const Divider = styled.View`
  width: 100%;
  height: 2px;
  background-color: #8c8c8c;
  margin-top: 10px;
  margin-left: 5px;
  margin-right: 5px;
  border-radius: 50px;
`;
const Item = styled.View`
  height: 50px;
  width: 100%;
  background-color: #fff;
  border-radius: 5px;
  justify-content: space-between;
  align-items: center;
  flex-flow: row;
  padding: 10px;
`;

const NoEvents = styled.View`
  flex: 1;
  justify-content: center;
  align-items: center;
`;

const Time = styled.Text`
  flex-shrink: 0;
`;

const Title = styled.Text`
  max-width: 210px;
`;