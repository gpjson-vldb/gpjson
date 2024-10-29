const fs = require(`fs`);
const simdjson = require('simdjson');
const readline = require('readline');

function init() {}

// $.user.lang
async function queryTT1(dataset) {
    var lineReader = readline.createInterface({ input: fs.createReadStream(dataset) });

    var result = [];
    for await (const line of lineReader) {
        try {
            const jsonTape = simdjson.lazyParse(line);
            let value = jsonTape.valueForKeyPath(`user.lang`);
            result.push(value);
        } catch (error) {
            // console.log(error);
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
            const jsonTape = simdjson.lazyParse(line);
            try {
                let value = jsonTape.valueForKeyPath(`user.lang`);
                result.push(value);
            } catch (error) {
                // console.log(error);
            }
            try {
                let value = jsonTape.valueForKeyPath(`lang`);
                result.push(value);
            } catch (error) {
                // console.log(error);
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
            const jsonTape = simdjson.lazyParse(line);
            let value = jsonTape.valueForKeyPath(`user.lang`);
            if (value == "nl")
                result.push(value);
        } catch (error) {
            // console.log(error);
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
            const jsonTape = simdjson.lazyParse(line);
            let value = jsonTape.valueForKeyPath(`user.lang`);
            if (value == "en")
                result.push(value);
        } catch (error) {
            // console.log(error);
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
            const jsonTape = simdjson.lazyParse(line);
            try {
                let value = jsonTape.valueForKeyPath(`bestMarketplacePrice.price`);
                result.push(value);
            } catch (error) {
                // console.log(error);
            }
            try {
                let value = jsonTape.valueForKeyPath(`name`);
                result.push(value);
            } catch (error) {
                // console.log(error);
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
            const jsonTape = simdjson.lazyParse(line);
            try {
                let value = jsonTape.valueForKeyPath(`categoryPath[1].id`);
                result.push(value);
            } catch (error) {
                // console.log(error);
            }
            try {
                let value = jsonTape.valueForKeyPath(`categoryPath[2].id`);
                result.push(value);
            } catch (error) {
                // console.log(error);
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