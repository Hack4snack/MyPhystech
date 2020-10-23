const tmpInfo = {
  firstTime: true
};

const user = (state={info: null, isLoading: false, error: null}, action) => {
  console.log(action);
  switch (action.type) {
    case 'SIGN_IN_REQUEST':
      return {...state, isLoading: true};
    case 'SIGN_IN_SUCCESS':
      return {...state, isLoading: false, info: action.payload.data};
    case 'SIGN_IN_FAILURE':
      return {...state, isLoading: false, error: action.error.response.message, info: tmpInfo};

    default:
      return state;
  }
};

export default user;