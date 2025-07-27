const _firebaseConfig = {
  apiKey: process.env.FIREBASE_APIKEY, //;
  authDomain: process.env.FIREBASE_AUTHDOMAIN, //
  projectId: process.env.FIREBASE_PROJECT_ID, //
  storageBucket: process.env.FIREBASE_STORAGE_BUCKET, //
  messagingSenderId: process.env.FIREBASE_MSGSEND_ID, // 
  appId: process.env.FIREBASE_APP_ID, // "",
  measurementId: process.env.FIREBASE_MESUREMENT_ID, //
};


export  {_firebaseConfig};
