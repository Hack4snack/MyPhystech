const channels = (state={list: [], isLoading: false, error: null}, action) => {
  switch (action.type) {
    case 'FETCH_STUDY_CHANNELS_REQUEST':
      return {...state, isLoading: true};
    case 'FETCH_STUDY_CHANNELS_SUCCESS':
      return {...state, isLoading: false, list: action.payload.data};
    case 'FETCH_STUDY_CHANNELS_FAILURE':
      return {...state, isLoading: false, error: action.error.response.message};

    default:
      return state;
  }
};

export default channels;