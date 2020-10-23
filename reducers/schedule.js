import moment from 'moment';

let tempList = [
  {
    id: 1,
    start_time: new Date(2020, 8, 15, 12, 20),
    end_time: new Date(2020, 8, 15, 13, 45),
    title: 'Физика',
    description: 'Лекция по физике',
    location: 'Б. Физ.'
  },
  {
    id: 2,
    start_time: new Date(2020, 8, 15, 13, 55),
    end_time: new Date(2020, 8, 15, 15, 30),
    title: 'Математический анализ',
    description: 'Семинар',
    location: '403 ГК'
  },
  {
    id: 3,
    start_time: new Date(2020, 8, 16, 12, 20),
    end_time: new Date(2020, 8, 16, 13, 45),
    title: 'Диффуры',
    description: 'Лекция по дифференциальным уравнениям',
    location: 'Б. Хим.'
  },
];

const schedule = (state={list: tempList, isLoading: false, error: null, tempPersonal: []}, action) => {
  switch (action.type) {
    case 'FETCH_SCHEDULE_REQUEST':
      return {...state, isLoading: true};
    case 'FETCH_SCHEDULE_SUCCESS':
      return {...state, isLoading: false, list: action.payload.data.map(e => ({end_time: null, ...e, start_time: moment(e.start_time, 'HH:mm DD.MM.YYYY')})).concat(state.list).filter((e, i, arr) => i === arr.map(k => k.id).indexOf(e.id))};
    case 'FETCH_SCHEDULE_FAILURE':
      return {...state, isLoading: false, error: action.error.response.message};

    case 'ADD_TO_SCHEDULE':
      return {...state, isLoading: false, tempPersonal: state.tempPersonal.concat(action.id)};

    case 'FETCH_PERSONAL_REQUEST':
      return {...state, isLoading: true};
    case 'FETCH_PERSONAL_SUCCESS':
      return {...state, isLoading: false, list: state.list.concat(action.payload.data
          .map(e => ({
            end_time: null,
            ...e,
            start_time: moment(e.start_time, 'HH:mm DD.MM.YYYY'),
            tags: e.tags.filter(t => t !== 'deadline'),
            title: e.title || (e.tags.filter(t => t !== 'deadline') && e.tags.filter(t => t !== 'deadline')[0]) || 'Событие',
            public_name: e.public_name || 'Публикация',
            group_img_url: e.group_img_url || 'https://png.pngtree.com/thumb_back/fw800/background/20190223/ourmid/pngtree-full-3d-radial-gradient-background-redcreative-backgroundcolored-radiation-image_84559.jpg',
            event_img_url: e.event_img_url || 'https://png.pngtree.com/thumb_back/fw800/back_our/20190628/ourmid/pngtree-geometric-wave-dots-seamless-background-image_265859.jpg',
          }))).filter((e, i, arr) => i === arr.map(k => k.id).indexOf(e.id))};
    case 'FETCH_PERSONAL_FAILURE':
      return {...state, isLoading: false, error: action.error.response.message};

    default:
      return state;
  }
};

export default schedule;