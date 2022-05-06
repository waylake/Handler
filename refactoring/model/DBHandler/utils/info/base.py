base_info = {
    'selenium': {
        'ops': {
            'headless',
            'ignore-certificate-errors',
            'dns-prefetch-disable',
            'disable-extensions',
        },
        'prefs': {'download.default_directory' : 'Data/chrome_driver'},
    },
    'dirs': [
        'Data',
        'Data/pkl',
        'Data/chrome_driver',
        'Data/chrome_driver',
    ],
}
