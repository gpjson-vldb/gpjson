const jp = require("jsonpath-plus");
const fs = require("fs");
const readline = require('readline');

function init() {}

// $.user.lang
async function queryTT1(dataset) {
    var lineReader = readline.createInterface({ input: fs.createReadStream(dataset) });

    var result = [];
    for await (const line of lineReader) {
        try {
            const obj = JSON.parse(line);
            let value = jp.JSONPath('$.user.lang', obj);
            for (let item of value) {
                result.push(item);
            }
        } catch (error) {
            console.log(error);
        }
    }
    return result;
}

// {$.user.lang, $.lang}
async function queryTT2(dataset) {
    var lineReader = readline.createInterface({ input: fs.createReadStream(dataset) });

    var result = [];
    for await (const line of lineReader) {
        try {
            const obj = JSON.parse(line);
            try {
                let value = jp.JSONPath('$.user.lang', obj);
                for (let item of value) {
                    result.push(item);
                }
            } catch (error) {
                console.log(error);
            }
            try {
                let value = jp.JSONPath('$.lang', obj);
                for (let item of value) {
                    result.push(item);
                }
            } catch (error) {
                console.log(error);
            }
        } catch { }
    }
    return result;
}

// $.user.lang[?(@ == 'nl')]"
async function queryTT3(dataset) {
    var lineReader = readline.createInterface({ input: fs.createReadStream(dataset) });

    var result = [];
    for await (const line of lineReader) {
        try {
            const obj = JSON.parse(line);
            let value = jp.JSONPath('$.user.lang', obj);
            if (value == "nl")
                for (let item of value) {
                    result.push(item);
                }
        } catch (error) {
            console.log(error);
        }
    }
    return result;
}

// $.user.lang[?(@ == 'en')]"
async function queryTT4(dataset) {
    var lineReader = readline.createInterface({ input: fs.createReadStream(dataset) });

    var result = [];
    for await (const line of lineReader) {
        try {
            const obj = JSON.parse(line);
            let value = jp.JSONPath('$.user.lang', obj);
            if (value == "en")
                for (let item of value) {
                    result.push(item);
                }
        } catch (error) {
            console.log(error);
        }
    }
    return result;
}

// {$.bestMarketplacePrice.price, $.name}
async function queryWM(dataset) {
    var lineReader = readline.createInterface({ input: fs.createReadStream(dataset) });

    var result = [];
    for await (const line of lineReader) {
        try {
            const obj = JSON.parse(line);
            try {
                let value = jp.JSONPath('$.bestMarketplacePrice.price', obj);
                for (let item of value) {
                    result.push(item);
                }
            } catch (error) {
                console.log(error);
            }
            try {
                let value = jp.JSONPath('$.name', obj);
                for (let item of value) {
                    result.push(item);
                }
            } catch (error) {
                console.log(error);
            }
        } catch { }
    }
    return result;
}

// $.categoryPath[1:3].id
async function queryBB(dataset) {
    var lineReader = readline.createInterface({ input: fs.createReadStream(dataset) });

    var result = [];
    for await (const line of lineReader) {
        try {
            const obj = JSON.parse(line);
            try {
                let value = jp.JSONPath('$.categoryPath[1:3].id', obj);
                for (let item of value) {
                    result.push(item);
                }
            } catch (error) {
                console.log(error);
            }
        } catch { }
    }
    return result;
}

function count(result) {
    return result.length;
}

module.exports = {
    init, count, queryTT1, queryTT2, queryTT3, queryTT4, queryWM, queryBB
}