ERR_LIST = ['SeleniumErr', 'Urllib3Err', 'RequestErr']


ERR_INFO = {
    'SeleniumErr': {
        'func': 'SeleniumErrList'
    },

    'Urllib3Err': {
        'func': 'Urllib3ErrList'
    },

    'RequestErr':{
        'func': 'RequestsErrList'
    },
}
