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
            for (var key1 in obj) {
                if (obj.hasOwnProperty(key1) && key1 == "user") {
                    for (var key2 in obj[key1]) {
                        if (obj[key1].hasOwnProperty(key2) && key2 == "lang") {
                            value = obj[key1][key2];
                            result.push(value);
                        }
                    }
                }
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
            for (var key1 in obj) {
                if (obj.hasOwnProperty(key1) && key1 == "user") {
                    for (var key2 in obj[key1]) {
                        if (obj[key1].hasOwnProperty(key2) && key2 == "lang") {
                            value = obj[key1][key2];
                            result.push(value);
                        }
                    }
                }
                if (obj.hasOwnProperty(key1) && key1 == "lang") {
                    value = obj[key1];
                    result.push(value);
                }
            }
        } catch (error) {
            console.log(error);
        }
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
            for (var key1 in obj) {
                if (obj.hasOwnProperty(key1) && key1 == "user") {
                    for (var key2 in obj[key1]) {
                        if (obj[key1].hasOwnProperty(key2) && key2 == "lang" && obj[key1][key2] == "nl") {
                            value = obj[key1][key2];
                            result.push(value);
                        }
                    }
                }
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
            for (var key1 in obj) {
                if (obj.hasOwnProperty(key1) && key1 == "user") {
                    for (var key2 in obj[key1]) {
                        if (obj[key1].hasOwnProperty(key2) && key2 == "lang" && obj[key1][key2] == "en") {
                            value = obj[key1][key2];
                            result.push(value);
                        }
                    }
                }
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
            for (var key1 in obj) {
                if (obj.hasOwnProperty(key1) && key1 == "bestMarketplacePrice") {
                    for (var key2 in obj[key1]) {
                        if (obj[key1].hasOwnProperty(key2) && key2 == "price") {
                            value = obj[key1][key2];
                            result.push(value);
                        }
                    }
                }
                if (obj.hasOwnProperty(key1) && key1 == "name") {
                    value = obj[key1];
                    result.push(value);
                }
            }
        } catch (error) {
            console.log(error);
        }
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
            for (var key1 in obj) {
                if (obj.hasOwnProperty(key1) && key1 == "categoryPath") {
                    for (var j = 1; j < 3 && j < obj[key1].length; j++) {
                        for (var key2 in obj[key1][j]) {
                            if (obj[key1][j].hasOwnProperty(key2) && key2 == "id") {
                                value = obj[key1][j][key2];
                                result.push(value);
                            }
                        }
                    }
                }
            }
        } catch (error) {
            console.log(error);
        }
    }
    return result;
}

function count(result) {
    return result.length;
}

module.exports = {
    init, count, queryTT1, queryTT2, queryTT3, queryTT4, queryWM, queryBB
}