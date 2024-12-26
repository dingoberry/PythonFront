jsdom = require('jsdom')

const { JSDOM, ResourceLoader } = jsdom;

// class CustomResourceLoader extends ResourceLoader {
//     fetch(url, options) {
//       // Override the contents of this script to do something unusual.
//     //   if (url === "https://example.com/some-specific-script.js") {
//     //     return Promise.resolve(Buffer.from("window.someGlobal = 5;"));
//     //   }
    
//       return Promise.resolve(Buffer.from('window.navigator.vendor = "Google Inc.";'));
//     }
//   }

// const resourceLoader = new CustomResourceLoader({
//     // proxy: "http://127.0.0.1:9001",
//     // strictSSL: false,
//     userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
//     vendor: "Google Inc."

// });

const dom = new JSDOM(`<!DOCTYPE html><header></header><body></body></html>`, {
    url: 'https://www.hermes.cn/cn/zh/',
    referrer: 'https://www.hermes.cn/cn/zh/',
    // resources: resourceLoader
});

// Object.defineProperties(dom.window, {
//     navigator: {
//         value: {
//             userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
//         }
//     }
// })

// Object.defineProperties(dom.window.navigator, {
//     userAgent: {
//         value: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
//         configurable: true,
//         enumerable: true,
//         writable: true
//     }
// })

function Base(){
    this.getDigName = function() {
        return "I m dig";
    };
    this.appName= "123";
};

function Geo(name){
    this.cxx = 'joker'
    this.name = name
}
Geo.prototype = new Base();
let bigbang = new Geo("wh");
// bigbang.prototype = undefined;
Object.defineProperty(bigbang, 'color', {
    value: "smooth",
    configurable: true
})

Object.defineProperty(Base, 'newValue', {
    value: "newValue",
    configurable: true
})
// bigbang.prototype.aa = function() {
//     return "12321"
// }

const sealObj = Object.create(function() {
    let o = {
        age: 13,
        name: '12'
    };
    Object.defineProperty(o, 'name', {
        value: 'xiaohuaxxx3',
        configurable: true,
        enumerable: true,
        writable: true
    })
    return o;
}());

// Object.defineProperty(sealObj, 'name', {value: "good"});
delete sealObj.__proto__.name;

const window = dom.window;
const document = window.document;
const location = window.location;
const navigator = window.navigator;

function execute() {
    // return `${JSON.stringify(document)}\n${document.referrer}\n${JSON.stringify(location)}\n${
    //     function(){
    //         let desc = '--Navigator--\n';
    //         desc += Object.getOwnPropertyDescriptor(window, 'navigator').configurable + "\n";
    //         for (let key in navigator) {
    //             desc += `"${key}":"${typeof navigator[key] === 'object' ? function(obj){
    //                 return obj;
    //             }(navigator[key]) : navigator[key]}"\n`;
    //         }
    //         desc += '--Navigator--\n';
    //         return desc;
    //     }()
    // }--${function() {
    //     let desc = '--Prototype--\n';
    //     let p = Object.getPrototypeOf(window);
    //     for (let key in p) {
    //         desc += `${key}\n`;
    //     }
    //     desc += `${window.prototype}`;
    //     return desc;
    // }()}`;
    // Object.setPrototypeOf(bigbang, new Object());
    return `${bigbang.prototype}-${bigbang.color}-${sealObj.name}`;
}