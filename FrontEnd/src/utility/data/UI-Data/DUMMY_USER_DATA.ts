import { _user_details } from "../../../models/types/userType";

const DUMMY_USER_INFO: _user_details[] = [
    {_id: 'EMP_ACC_WV_EMPID' , _name:'Trevor Stevenson', _badge_ID:'387923782', _account: 'ACCT_X', _position:'Supervisor', _wave:'01', _assistance: 'Logged-In'
        // _assistance:{_id:'EMP_ACC_WV_EMPID', _clock_in: Date.now., _clock_break,  _clock_lunch, _clock_out}
        },
]



type _user_asistance = {
        _id: string;
        _clock_in: Date;
        _clock_out: Date;
        _clock_lunch: Date;
        _clock_break: Date;
}

export {DUMMY_USER_INFO};