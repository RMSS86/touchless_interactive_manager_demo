export const useLogger = ({
  _module,
  _value,
}: {
  _module: string;
  _value: any;
}) => {
  console.log("FROM " + _module + ": ", _value);
};
