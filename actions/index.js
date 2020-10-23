export function fetchEvents({token, limit, offset}) {
  let type = 'FETCH_EVENTS';
  return {
    types: [`${type}_REQUEST`, `${type}_SUCCESS`, `${type}_FAILURE`],
    payload: {
      request:{
        url:'/event/filter',
        method: 'GET',
        params: {
          tags: 'deadline'
        },
        headers: {
          'Authorization': `Bearer ${token}`
        }
      }
    }
  }
}

export function fetchSchedule({token, month, group}) {
  let type = 'FETCH_SCHEDULE';
  return {
    types: [`${type}_REQUEST`, `${type}_SUCCESS`, `${type}_FAILURE`],
    payload: {
      request:{
        url:'/event/filter',
        method: 'GET',
        params: {
          tags: 'Б01-901'
        },
        headers: {
          'Authorization': `Bearer ${token}`
        }
      }
    }
  }
}

export function fetchPersonal({ids, token}) {
  let type = 'FETCH_PERSONAL';
  return {
    types: [`${type}_REQUEST`, `${type}_SUCCESS`, `${type}_FAILURE`],
    payload: {
      request:{
        url:'/event/by_id',
        method: 'GET',
        params: {
          id: ids.join('')
        },
        headers: {
          'Authorization': `Bearer ${token}`
        }
      }
    }
  }
}

export function addToSchedule({id}) {
  return (dispatch, getState) => {
    dispatch(fetchPersonal({ids: getState().schedule.tempPersonal.concat(id)}))
      .then(() => {
        return {
          type: 'ADD_TO_SCHEDULE',
          id
        };
      });
  };
}

export function signIn({idToken}) {
  let type = 'SIGN_IN';
  return {
    types: [`${type}_REQUEST`, `${type}_SUCCESS`, `${type}_FAILURE`],
    payload: {
      request:{
        url:'/auth/signin',
        method: 'POST',
        params: {
          idToken
        }
      }
    }
  }
}

export function fetchStudyChannels({limit, offset, text}) {
  let type = 'FETCH_STUDY_CHANNELS';
  return {
    types: [`${type}_REQUEST`, `${type}_SUCCESS`, `${type}_FAILURE`],
    payload: {
      request:{
        url:'/topics/channel',
        method: 'GET',
        params: {
          is_study_group: 1,
          limit,
          offset,
          search_text: text
        }
      }
    }
  }
}