import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, Image, TextInput } from 'react-native';
import styled from 'styled-components/native';
import IconAnt from 'react-native-vector-icons/AntDesign';
import IconF from 'react-native-vector-icons/Feather';
import { Badge } from 'react-native-elements';
import LikeButton from "./LikeButton";
import AddToCalendarButton from "./AddToCalendarButton";

const maxLimit = 88;

export default function Event() {
  const [ expanded, setExpanded ] = useState(false);
  const [ liked, setLiked ] = useState(false);
  const [ added, setAdded ] = useState(false);
  const fullText = 'Сегодня снова под девяткой всех желающих ждет возможность покидать мячик. Сетка тоже есть. Начало с 19.30.';

  return (
    <Wrapper>
      <UpperLine>
        <Public>
          <PublicAvatar source={{uri: 'https://sun1-30.userapi.com/c624827/v624827921/2d963/3VDSs6ocPks.jpg?ava=1'}}></PublicAvatar>
          <PublicTitle>Любительский волейбол МФТИ</PublicTitle>
        </Public>
        <PublicationDate>2ч назад</PublicationDate>
      </UpperLine>
      <Preview source={{uri: 'https://img4.goodfon.ru/wallpaper/nbig/4/2d/low-poly-voleibol-igra-miach-sportsmen-voleibolist.jpg'}}></Preview>
      <View style={{flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center'}}>
        <LikeButton liked={liked} setLiked={setLiked} />
        <AddToCalendarButton added={added} setAdded={setAdded} />
      </View>
      <Title>
        Вечером возле 4-ки
      </Title>
      <Info>
        <Tag>Спорт</Tag>
        <Time>Завтра, 11:00 - 12:30</Time>
      </Info>
      <FullText>
        {fullText.length > maxLimit && !expanded ?
          <Text>{fullText.substring(0, maxLimit-3)}<More onPress={() => setExpanded(true)}>...еще</More></Text> :
          <Text>{fullText}</Text> }
      </FullText>
    </Wrapper>
  );
}

const Wrapper = styled.View`
  width: 100%;
  background: #1E2631;
  padding: 15px;
`;

const UpperLine = styled.View`
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
`;

const Public = styled.View`
  flex: 1;
  flex-direction: row;
  align-items: center;
`;

const PublicAvatar = styled.Image`
  width: 30px;
  height: 30px;
  border-radius: 50px;
  margin-right: 10px;
`;

const PublicTitle = styled.Text`
  color: white;
  font-family: Roboto;
  font-weight: 600;
`;

const PublicationDate = styled.Text`
  color: #5A677F;
  font-family: Roboto;
  font-weight: 600;
`;

const Preview = styled.Image`
  width: 100%;
  height: 200px;
  border-radius: 15px;
  margin-bottom: 10px;
`;

const Tag = styled.Text`
  color: #FF5045;
  font-weight: bold;
`;

const Time = styled.Text`
  color: #5A677F
`;

const Title = styled.Text`
  color: white;
  font-family: Montserrat;
  font-size: 20px;
  font-weight: bold;
  margin-top: 0px;
`;

const FullText = styled.Text`
  color: white;
  font-size: 13px;
`;

const More = styled.Text`
  color: #c1c1c1;
`;

const Info = styled.View`
  flex-direction: row;
  justify-content: space-between;
  margin-bottom: 3px;
  margin-top: 3px;
`;