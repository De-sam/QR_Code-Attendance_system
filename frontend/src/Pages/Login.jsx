import React, { useState } from 'react';
import './Login.css';
import InputField from './../library/components/InputField/index';
import { Validators } from './../library/utilities/Validator';

function Login() {
	const [value, setValue] = useState('');

	const handleChange = (value) => {
		console.log(value);
		setValue(value)
	}

	return (
		<div>
		<InputField 
		value={value} 
		placeholder="Enter Username" 
		onChange={handleChange}
		type="text"
		label="Username:" 
		validators={[{
			check: Validators.required, 
			message: "Username is required"}]
		} />

		<InputField 
		value={value} 
		placeholder="Password" 
		onChange={handleChange}
		type="password"
		label="Password:" 
		validators={[{
			check: Validators.required, 
			message: "Password is required"}]
		} />
		</div>
	)
}

export default Login