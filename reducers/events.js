import moment from 'moment';

let tempList = [
  {
    id: 1,
    title: 'Вечером возле 4-ки',
    tags: ['Спорт'],
    description: 'Сегодня снова под девяткой всех желающих ждет возможность покидать мячик. Сетка тоже есть. Начало с 19.30.',
    start_time: new Date(2020, 8, 16, 17, 5),
    end_time: new Date(2020, 8, 16, 18, 30),
    group_img_url: 'https://sun1-30.userapi.com/c624827/v624827921/2d963/3VDSs6ocPks.jpg?ava=1',
    event_img_url: 'https://img4.goodfon.ru/wallpaper/nbig/4/2d/low-poly-voleibol-igra-miach-sportsmen-voleibolist.jpg',
    public_name: 'Любительский волейбол МФТИ',
    publication_time: new Date(2020, 8, 13, 18, 30),
  },
  {
    id: 2,
    title: 'Вечером возле 4-ки',
    tags: ['Спорт'],
    description: 'Сегодня снова под девяткой всех желающих ждет возможность покидать мячик. Сетка тоже есть. Начало с 19.30.',
    start_time: new Date(2020, 8, 16, 17, 5),
    end_time: new Date(2020, 8, 16, 18, 30),
    group_img_url: 'https://sun1-30.userapi.com/c624827/v624827921/2d963/3VDSs6ocPks.jpg?ava=1',
    event_img_url: 'https://img4.goodfon.ru/wallpaper/nbig/4/2d/low-poly-voleibol-igra-miach-sportsmen-voleibolist.jpg',
    public_name: 'Любительский волейбол МФТИ',
    publication_time: new Date(2020, 8, 13, 18, 30),
  }
];

const events = (state={list: tempList, isLoading: false, error: null}, action) => {
  switch (action.type) {
    case 'FETCH_EVENTS_REQUEST':
      return {...state, isLoading: true};
    case 'FETCH_EVENTS_SUCCESS':
      return {...state, isLoading: false, list: action.payload.data.map(e => ({
          end_time: null,
          ...e,
          start_time: (e.start_time && moment(e.start_time, 'HH:mm DD.MM.YYYY').toDate()) || moment().toDate(),
          tags: e.tags.filter(t => t !== 'deadline'),
          title: e.title || (e.tags.filter(t => t !== 'deadline') && e.tags.filter(t => t !== 'deadline')[0]) || 'Событие',
          public_name: e.public_name || 'Публикация',
          group_img_url: e.group_img_url || 'https://png.pngtree.com/thumb_back/fw800/background/20190223/ourmid/pngtree-full-3d-radial-gradient-background-redcreative-backgroundcolored-radiation-image_84559.jpg',
          event_img_url: e.event_img_url || 'https://png.pngtree.com/thumb_back/fw800/back_our/20190628/ourmid/pngtree-geometric-wave-dots-seamless-background-image_265859.jpg',
      }))};
    case 'FETCH_EVENTS_FAILURE':
      return {...state, isLoading: false, error: action.error.response.message};

    default:
      return state;
  }
};

export default events;