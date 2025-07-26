import { useState } from "react";

export default function NavHolder({
  HolderContainer = "div",
  className,

  _inputType,
  _inputId,
  _inputClass,
  _btnFor,
  _btnClass,
  _iconClass,
  _bgClass,
  children,
  _id,
  ...props
}) {
  const [name, setName] = useState();

  return (
    <HolderContainer id={_id} className={className} {...props}>
      <input type={_inputType} className={_inputClass} id={_inputId} />
      <label htmlFor={_btnFor} className={_btnClass}>
        <span className={_iconClass}>&nbsp;</span>
      </label>
      <div className={_bgClass}>&nbsp;</div>
      {children}
    </HolderContainer>
  );
}
