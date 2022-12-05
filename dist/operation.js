"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.calculation = void 0;
const calculation = (req, res, next) => {
    let { operation_type, x, y } = req.body;
    const operation = (operation_type, x, y) => {
        if (operation_type === 'ADD') {
            return x + y;
        }
        else if (operation_type === 'SUBTRACT') {
            return x - y;
        }
        else if (operation_type === 'MULTIPLY') {
            return x * y;
        }
        else {
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
exports.calculation = calculation;
