db_info = {
    'RAW': {
        'host': 'medic-db-dev.c6dzc5dnqf69.ap-northeast-2.rds.amazonaws.com',
        'user': 'mediai_db_admin',
        'passwd': 'EXJ=cL}imH',
        'port': 33066,
    },
}

table_list = [
    'guideline_ema',
]

table_info = {
    'scheme': {
        'guideline_ema': [
            'guideline_id',
            'reference_number',
            'title',
            'publish_date',
            'status',
            'effective_form',
            'keywords',
            'description',
            'file_attachment',
            'url',
            'create_date',
            'update_date'
        ],

        'to_scheme': {
            'guideline_id': 'guideline_id',
            'reference_number' : 'reference_number',
            'title': 'title',
            'publish_date': 'publish_date',
            'status' : 'status',
            'effective_form' : 'effective_form',
            'keywords' : 'keywords',
            'description': 'description',
            'file_attachment': 'file_attachment',
            'url': 'url',
        },
    },
}
