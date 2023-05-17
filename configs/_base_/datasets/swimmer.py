dataset_info = dict(
    dataset_name='swimmer',
    keypoint_info={
        0:
        dict(
            name='Head',
            id=0,
            color=[51, 153, 255],
            type='upper'),
        1:
        dict(
            name='LShoulder',
            id=1,
            color=[0, 255, 0],
            type='upper',
            swap='RShoulder'),
        2:
        dict(
            name='LElbow',
            id=2,
            color=[0, 255, 0],
            type='upper',
            swap='RElbow'),
        3:
        dict(
            name='LWrist',
            id=3,
            color=[0, 255, 0],
            type='upper',
            swap='RWrist'),
        4:
        dict(
            name='RShoulder',
            id=4,
            color=[255, 128, 0],
            type='upper',
            swap='LShoulder'),
        5:
        dict(
            name='RElbow',
            id=5,
            color=[255, 128, 0],
            type='upper',
            swap='LElbow'),
        6:
        dict(
            name='RWrist',
            id=6,
            color=[255, 128, 0],
            type='upper',
            swap='LWrist'),
        7:
        dict(
            name='LHip',
            id=7,
            color=[156, 10, 39],
            type='lower',
            swap='RHip'),
        8:
        dict(
            name='LKnee',
            id=8,
            color=[156, 100, 200],
            type='lower',
            swap='RKnee'),
        9:
            dict(
                name='LAnkle',
                id=9,
                color=[0, 100, 200],
                type='lower',
                swap='RAnkle'),

        10:
            dict(
                name='RHip',
                id=10,
                color=[0, 255, 56],
                type='lower',
                swap='LHip'),
        11:
            dict(
                name='RKnee',
                id=11,
                color=[0, 255, 56],
                type='lower',
                swap='LKnee'),
        12:
            dict(
                name='RAnkle',
                id=12,
                color=[0, 255, 56],
                type='lower',
                swap='LAnkle'),
    },
    skeleton_info={
        0:
        dict(link=('Head', 'LShoulder'), id=0, color=[0, 255, 0]),
        1:
        dict(link=('Head', 'RShoulder'), id=1, color=[0, 255, 0]),
        2:
        dict(link=('LShoulder', 'LElbow'), id=2, color=[255, 128, 0]),
        3:
        dict(link=('LElbow', 'LWrist'), id=3, color=[255, 128, 0]),
        4:
        dict(link=('RShoulder', 'RElbow'), id=4, color=[51, 153, 255]),
        5:
        dict(link=('RElbow', 'RWrist'), id=5, color=[51, 153, 255]),
        6:
        dict(link=('LHip', 'LShoulder'), id=6, color=[0, 153, 255]),
        7:
        dict(link=('LHip', 'LKnee'), id=7, color=[51, 0, 255]),
        8:
        dict(link=('LKnee', 'LAnkle'), id=8, color=[51, 153, 0]),
        9:
        dict(link=('RHip', 'RShoulder'), id=9, color=[0, 153, 255]),
        10:
        dict(link=('RHip', 'RKnee'), id=10, color=[51, 0, 255]),
        11:
        dict(link=('RKnee', 'RAnkle'), id=11, color=[51, 153, 0])
    },
    joint_weights=[
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.
    ],
    sigmas=[0.026, 0.079, 0.072, 0.062, 0.079, 0.072, 0.062, 0.107, 0.087, 0.089, 0.107, 0.087, 0.089])
