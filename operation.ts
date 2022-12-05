import {Request, Response, NextFunction} from 'express'

export const calculation = (req:Request, res:Response, next:NextFunction) => {
	let { operation_type, x, y } = req.body;
	const operation = (operation_type:string, x:number, y:number) => {
		if (operation_type === 'ADD') {
			return x + y;
		} else if (operation_type === 'SUBTRACT') {
			return x - y;
		} else if (operation_type === 'MULTIPLY') {
			return x * y;
		} else {
			return `operation is not valid for ${x} and ${y}`;
		}
	};
	const result = operation(operation_type, x, y);
	return res.status(201).json({
		slackUsername: 'davidadediji',
		result: result,
		operation_type: operation_type,
	});
	next();
};
