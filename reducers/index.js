import { combineReducers } from 'redux';
import events from './events';
import schedule from './schedule';
import user from './user';
import channels from './channels';

export default combineReducers({
  events,
  schedule,
  user,
  channels,
});