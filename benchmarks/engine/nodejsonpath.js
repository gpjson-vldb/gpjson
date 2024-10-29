const jp = require("jsonpath");
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
            let value = jp.query(obj, '$.user.lang');
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
                let value = jp.query(obj, '$.user.lang');
                for (let item of value) {
                    result.push(item);
                }
            } catch (error) {
                console.log(error);
            }
            try {
                let value = jp.query(obj, '$.lang');
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
            let value = jp.query(obj, '$.user.lang');
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
            let value = jp.query(obj, '$.user.lang');
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
                let value = jp.query(obj, '$.bestMarketplacePrice.price');
                for (let item of value) {
                    result.push(item);
                }
            } catch (error) {
                console.log(error);
            }
            try {
                let value = jp.query(obj, '$.name');
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
                let value = jp.query(obj, '$.categoryPath[1:3].id');
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
