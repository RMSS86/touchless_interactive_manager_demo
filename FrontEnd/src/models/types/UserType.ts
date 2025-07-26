type User = {
  _id?: string;
  _role: "user" | "guide" | "admin";
  _active: boolean;
  _name: string;
  _email: string; //create type email for email validation
  _passwordChangedAt: string;
  _token?: string;
  _imgDir?: string;
  _photo?: string;
  _img?: ImageBitmap | File | string | HTMLImageElement;
};

type NewUser = {
  _name: string;
  _email: string;
  _password: string;
  _passwordConfirm: string;
};

type PasswordReset = {
  password: string;
  passwordConfirm: string;
  passwordResetToken: string;
  passwordResetExpires: string;
};
type PasswordUpdate = {
  passwordCurrent: string;
  password: string;
  passwordConfirm: string;
};
type Login = {
  email: string;
  password: string;
};
type UpdateUser = {
  name: string;
  email: string;
  photo: File | undefined;
};
type Email = {
  email: string;
};
export type {
  User,
  NewUser,
  PasswordReset,
  Login,
  UpdateUser,
  PasswordUpdate,
  Email,
};

// {
//   "status": "success",
//   "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY3OTFhNDYyZTk5M2NiMDE1YmE2NTMzOSIsImlhdCI6MTc0MTk5Mjc4NywiZXhwIjoxNzQ5NzY4Nzg3fQ.DZBBgKrbCQXOxgt1_FxvjZLfhpVKPieXhirkeP8XiXo",
//   "data": {
//       "user": {
//           "_id": "6791a462e993cb015ba65339",
//           "role": "user",
//           "name": "Scott R. Trevor",
//           "email": "scottsland14@gmail.com",
//           "__v": 0,
//           "passwordChangedAt": "2025-01-25T04:01:13.465Z"
//       }
//   }
// }
