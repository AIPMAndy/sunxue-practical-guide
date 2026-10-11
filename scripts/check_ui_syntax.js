// Optional test for homepage interactive JavaScript syntax. Requires Node.js.
const fs=require('fs');const vm=require('vm');
const html=fs.readFileSync(require('path').join(__dirname,'../index.html'),'utf8');
const scripts=[...html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/gi)];
if(scripts.length!==1) throw new Error('Homepage must have exactly one inline script');
for(const [,code] of scripts){new vm.Script(code)}
if((html.match(/data-day=\"[0-6]\"/g)||[]).length!==7)throw new Error('Expected 7 tasks');
console.log('PASS: homepage JavaScript parsed and seven tasks present');
