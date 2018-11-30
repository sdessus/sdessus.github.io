/**
 * Fastly Insights.js
 * Build generated: 2018-11-26
 * https://github.com/fastly/insights.js
 *
 * Copyright (c) 2018, Fastly, Inc. All rights reserved.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

!function(){"use strict";function t(t,e){return e.split(".").every(function(e){return"object"===(void 0===t?"undefined":o(t))&&null!==t&&e in t&&void 0!==t[e]&&(t=t[e],!0)})}function e(){var t=document.getElementsByTagName("script")[0],e=document.createElement("script");e.src=n.build,e.onload=function(){"function"==typeof window.FASTLY.init&&window.FASTLY.init(n)},t.parentNode.insertBefore(e,t)}var n={apiKey:"6a52360a-f306-421e-8ed5-7417d0d4a4e9",session:"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2YTUyMzYwYS1mMzA2LTQyMWUtOGVkNS03NDE3ZDBkNGE0ZTkiLCJleHAiOjE1NDM1MDk5MTAsImlhdCI6MTU0MzUwOTg1MX0.M9A0xJUJglnIafS3UX5s9omPSHprhXaThmLILIG7X4Q",settings:{"hosts": {"host": "www.fastly-insights.com","lookup": "apac.u.fastly-insights.com","pop": "pops.fastly-insights.com",},"sample":1.000},build:"https://www.fastly-insights.com/static/lib.57fc086d415181e02aa3aea47f453b6cf7883d95.js",server:{"datacenter": "SIN"},tasks:[{"id": "pdata","type": "fetch","host": "pdata.pops.fastly-insights.com"}],pops:['SIN', 'HKG', 'TYO', 'HND', 'NRT', 'ITM', 'SYD', 'PAO', 'SJC', 'LAX', 'BUR', 'CDG', 'MAD', 'FRA', 'LCY', 'HHN', 'AKL', 'SEA', 'AMS', 'DEN', 'MEL', 'WLG', 'BMA', 'FJR', 'YVR', 'MAA', 'DFW', 'BOM', 'IAH', 'MDW', 'MSP', 'ATL', 'ORD', 'PDK', 'LHR', 'YYZ', 'IAD', 'DCA', 'CMH', 'BWI', 'EWR', 'BNE', 'YUL', 'MIA', 'JFK', 'BOS', 'HEL', 'PER', 'CPT', 'CWB', 'JNB', 'GIG', 'SCL', 'EZE', 'GRU']},o="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t},i=n.ctm=t(window,"Promise")&&t(window,"Set")&&t(window,"fetch")&&t(window,"performance.getEntries");i&&function(t){return parseFloat(Math.random().toFixed(2))<=t}(n.settings.sample)&&function(t){"complete"!==document.readyState?document.addEventListener("readystatechange",function(){"complete"===document.readyState&&t()}):t()}(function(){return setTimeout(e,n.settings.delay||0)}),window.FASTLY=window.FASTLY||{},window.FASTLY.ctm=i,window.FASTLY.config=n}();
