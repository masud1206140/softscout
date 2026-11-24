# Articles for softscout.support. Each article has English and Bengali versions.
# Fields: slug, date (published), updated, and per language: title, desc, short (answer
# shown first), body (HTML), faq [(q, a)], sources [(label, url)].

ARTICLES = []

# ---------------------------------------------------------------------------
ARTICLES.append({
    "slug": "website-testing-checklist",
    "date": "2026-11-24", "updated": "2026-11-24",
    "en": {
        "title": "Website testing checklist: what to check before you launch",
        "desc": "A practical checklist for testing a website before and after launch: pages, forms, checkout, phones, content accuracy, speed, accessibility and tracking.",
        "short": "Before launch, test every page and form the way a new visitor would: on a phone and a computer, in at least two browsers, with real tasks such as signing up or buying. Check that text, prices and help pages match what is on screen, that forms really deliver, and that the site is fast and readable. Record each problem with a screenshot and the steps to repeat it.",
        "body": """
<h2>How to use this checklist</h2>
<p>Go through it with real tasks, not by clicking around. Pick the three or four things a visitor most often comes to do (find a product, ask for a quote, sign up, pay) and complete each one from start to finish. Do it once on a phone and once on a computer.</p>

<h2>1. Pages and navigation</h2>
<ul>
  <li>Every menu item opens the right page, on phone and computer.</li>
  <li>No broken links (pages that show an error or "not found").</li>
  <li>Unknown addresses show a helpful "page not found" page with a way back.</li>
  <li>The logo returns to the home page.</li>
  <li>Page titles in the browser tab are different for each page and describe it.</li>
</ul>

<h2>2. Forms and sign-up</h2>
<ul>
  <li>Each form sends, and the message actually arrives where it should (check the inbox, not just the "thank you" screen).</li>
  <li>Required fields are marked, and error messages say what to fix.</li>
  <li>Phone numbers, emails and names in your language are accepted.</li>
  <li>Sign-up, log-in and "forgot password" work end to end, including the email they send.</li>
  <li>Spam protection does not block real people.</li>
</ul>

<h2>3. Checkout and payment (if you sell online)</h2>
<ul>
  <li>The price on the product page matches the cart and the final total.</li>
  <li>Discounts, delivery charges and taxes are added correctly.</li>
  <li>The payment step works on iPhone and Android, not only on a computer.</li>
  <li>The confirmation page and email show the right order details.</li>
</ul>

<h2>4. Phones, tablets and browsers</h2>
<ul>
  <li>No sideways scrolling on a phone; text is readable without zooming.</li>
  <li>Buttons are big enough to tap and are not hidden behind cookie banners or chat bubbles.</li>
  <li>The site works in Chrome, Safari and at least one other browser.</li>
  <li>Images and videos load and fit the screen.</li>
</ul>

<h2>5. Content accuracy</h2>
<ul>
  <li>Product names, prices, phone numbers and addresses are correct and the same everywhere.</li>
  <li>Help pages and guides use the same button and menu names as the live screens.</li>
  <li>No placeholder text, test data or old offers left on the site.</li>
  <li>Claims such as "fastest" or "award-winning" can be backed up.</li>
  <li>Both language versions say the same thing, if your site has two languages.</li>
</ul>

<h2>6. Speed and accessibility basics</h2>
<ul>
  <li>Main pages open in a few seconds on a mobile connection.</li>
  <li>Images have short descriptions (alt text) that say what they show.</li>
  <li>Text has enough contrast against the background.</li>
  <li>You can move through the page with the keyboard and see where you are.</li>
</ul>

<h2>7. Search, AI assistants and tracking</h2>
<ul>
  <li>Each page has a clear title and a one-sentence description.</li>
  <li>A sitemap exists and <code>robots.txt</code> does not block pages you want found.</li>
  <li>Your hosting or security service is not blocking the search and AI crawlers you want.</li>
  <li>Analytics records visits once, not twice, and ignores your own test visits if possible.</li>
</ul>

<h2>8. After launch</h2>
<ul>
  <li>Repeat the main tasks on the live address, not only on the test site.</li>
  <li>Check that "www" and the plain address both work and that the padlock (HTTPS) shows.</li>
  <li>Send a test enquiry through every contact route and confirm it arrives.</li>
  <li>Check again after every big change; problems often come back with updates.</li>
</ul>

<h2>How to record what you find</h2>
<p>Write one line per problem with: the page, what you did, what you expected, what happened, a screenshot, the device and browser, and how serious it is. That way whoever fixes it does not need to ask you anything. Our guide on <a href="/articles/how-to-write-a-bug-report/">how to write a bug report</a> has a template.</p>
""",
        "faq": [
            ("How long does website testing take?", "For a small business site of 5 to 15 pages, a careful pass on phone and computer usually takes one to two working days, including writing up the findings. Shops and apps with log-ins take longer because each flow has to be completed end to end."),
            ("Can I test my own website?", "Yes, and you should. But people who built a site tend to follow the paths they know. A fresh tester, or a friend who has never seen it, finds different problems."),
            ("What should be fixed first?", "Anything that stops a visitor from completing the main task: broken forms, payment errors, wrong prices and wrong contact details. Cosmetic issues can wait."),
        ],
        "sources": [],
    },
    "bn": {
        "title": "ওয়েবসাইট টেস্টিং চেকলিস্ট: চালুর আগে কী কী যাচাই করবেন",
        "desc": "ওয়েবসাইট চালুর আগে ও পরে টেস্ট করার একটি ব্যবহারিক চেকলিস্ট: পাতা, ফর্ম, চেকআউট, ফোন, কনটেন্টের সঠিকতা, গতি, অ্যাক্সেসিবিলিটি ও ট্র্যাকিং।",
        "short": "চালুর আগে প্রতিটি পাতা ও ফর্ম একজন নতুন দর্শকের মতো টেস্ট করুন: ফোন ও কম্পিউটারে, অন্তত দুটি ব্রাউজারে, সাইন-আপ বা কেনাকাটার মতো আসল কাজ করে। লেখা, দাম ও হেল্প পাতা স্ক্রিনের সাথে মেলে কি না, ফর্ম সত্যিই পৌঁছায় কি না, এবং সাইট দ্রুত ও পড়ার উপযোগী কি না দেখুন। প্রতিটি সমস্যা স্ক্রিনশট ও পুনরায় ঘটানোর ধাপসহ লিখে রাখুন।",
        "body": """
<h2>চেকলিস্টটি কীভাবে ব্যবহার করবেন</h2>
<p>এলোমেলো ক্লিক না করে আসল কাজ ধরে এগোন। দর্শক সাধারণত যে তিন-চারটি কাজের জন্য আসেন (প্রোডাক্ট খোঁজা, দাম জানতে চাওয়া, সাইন-আপ, পেমেন্ট) সেগুলো শুরু থেকে শেষ পর্যন্ত করুন। একবার ফোনে, একবার কম্পিউটারে।</p>

<h2>১. পাতা ও নেভিগেশন</h2>
<ul>
  <li>প্রতিটি মেনু আইটেম ফোন ও কম্পিউটারে সঠিক পাতা খোলে।</li>
  <li>কোনো ভাঙা লিংক নেই (যে পাতা ত্রুটি বা "not found" দেখায়)।</li>
  <li>অজানা ঠিকানায় একটি সহায়ক "পাতা পাওয়া যায়নি" পাতা আসে, ফেরার পথসহ।</li>
  <li>লোগোতে চাপলে হোম পাতায় ফেরা যায়।</li>
  <li>ব্রাউজার ট্যাবে প্রতিটি পাতার শিরোনাম আলাদা এবং পাতার বিষয় বোঝায়।</li>
</ul>

<h2>২. ফর্ম ও সাইন-আপ</h2>
<ul>
  <li>প্রতিটি ফর্ম পাঠানো যায়, এবং বার্তা সত্যিই সঠিক জায়গায় পৌঁছায় (শুধু "ধন্যবাদ" স্ক্রিন নয়, ইনবক্স দেখুন)।</li>
  <li>আবশ্যক ঘর চিহ্নিত, এবং ত্রুটির বার্তায় লেখা থাকে কী ঠিক করতে হবে।</li>
  <li>ফোন নম্বর, ইমেইল ও বাংলায় লেখা নাম গ্রহণ করে।</li>
  <li>সাইন-আপ, লগ-ইন ও "পাসওয়ার্ড ভুলে গেছি" শুরু থেকে শেষ পর্যন্ত কাজ করে, পাঠানো ইমেইলসহ।</li>
  <li>স্প্যাম সুরক্ষা আসল মানুষকে আটকে দেয় না।</li>
</ul>

<h2>৩. চেকআউট ও পেমেন্ট (অনলাইনে বিক্রি করলে)</h2>
<ul>
  <li>প্রোডাক্ট পাতার দাম কার্ট ও চূড়ান্ত মোটের সাথে মেলে।</li>
  <li>ছাড়, ডেলিভারি চার্জ ও কর সঠিকভাবে যোগ হয়।</li>
  <li>পেমেন্টের ধাপ শুধু কম্পিউটারে নয়, আইফোন ও অ্যান্ড্রয়েডেও কাজ করে।</li>
  <li>নিশ্চিতকরণ পাতা ও ইমেইলে অর্ডারের তথ্য সঠিক থাকে।</li>
</ul>

<h2>৪. ফোন, ট্যাবলেট ও ব্রাউজার</h2>
<ul>
  <li>ফোনে পাশে স্ক্রল করতে হয় না; জুম না করেই লেখা পড়া যায়।</li>
  <li>বাটনগুলো চাপার মতো বড়, এবং কুকি ব্যানার বা চ্যাট বাবলের নিচে ঢাকা নয়।</li>
  <li>সাইট ক্রোম, সাফারি এবং অন্তত আরেকটি ব্রাউজারে কাজ করে।</li>
  <li>ছবি ও ভিডিও লোড হয় এবং স্ক্রিনে ঠিকমতো আঁটে।</li>
</ul>

<h2>৫. কনটেন্টের সঠিকতা</h2>
<ul>
  <li>প্রোডাক্টের নাম, দাম, ফোন নম্বর ও ঠিকানা সঠিক এবং সব জায়গায় এক।</li>
  <li>হেল্প পাতা ও গাইডে লাইভ স্ক্রিনের একই বাটন ও মেনুর নাম ব্যবহার হয়েছে।</li>
  <li>সাইটে কোনো ডামি লেখা, টেস্ট ডেটা বা পুরোনো অফার রয়ে যায়নি।</li>
  <li>"সবচেয়ে দ্রুত" বা "পুরস্কারপ্রাপ্ত" ধরনের দাবির প্রমাণ আছে।</li>
  <li>সাইট দুই ভাষায় হলে, দুই সংস্করণে একই কথা বলা আছে।</li>
</ul>

<h2>৬. গতি ও অ্যাক্সেসিবিলিটির মৌলিক বিষয়</h2>
<ul>
  <li>মোবাইল সংযোগে প্রধান পাতাগুলো কয়েক সেকেন্ডে খোলে।</li>
  <li>ছবির ছোট বর্ণনা (alt text) আছে, যা বলে ছবিতে কী দেখা যাচ্ছে।</li>
  <li>পটভূমির তুলনায় লেখা যথেষ্ট স্পষ্ট।</li>
  <li>কিবোর্ড দিয়ে পাতার মধ্যে চলা যায় এবং কোথায় আছেন বোঝা যায়।</li>
</ul>

<h2>৭. সার্চ, এআই সহকারী ও ট্র্যাকিং</h2>
<ul>
  <li>প্রতিটি পাতার স্পষ্ট শিরোনাম ও এক বাক্যের বর্ণনা আছে।</li>
  <li>সাইটম্যাপ আছে, এবং <code>robots.txt</code> এমন পাতা আটকায় না যা আপনি খুঁজে পাওয়াতে চান।</li>
  <li>আপনার হোস্টিং বা নিরাপত্তা সেবা আপনার কাঙ্ক্ষিত সার্চ ও এআই ক্রলারকে আটকাচ্ছে না।</li>
  <li>অ্যানালিটিক্স প্রতিটি ভিজিট একবারই গোনে, এবং সম্ভব হলে আপনার নিজের টেস্ট ভিজিট বাদ দেয়।</li>
</ul>

<h2>৮. চালুর পরে</h2>
<ul>
  <li>শুধু টেস্ট সাইটে নয়, লাইভ ঠিকানায় প্রধান কাজগুলো আবার করুন।</li>
  <li>"www" সহ ও ছাড়া দুই ঠিকানাই কাজ করে এবং তালা চিহ্ন (HTTPS) দেখায় কি না দেখুন।</li>
  <li>প্রতিটি যোগাযোগ মাধ্যমে একটি টেস্ট বার্তা পাঠিয়ে নিশ্চিত হোন তা পৌঁছায়।</li>
  <li>প্রতিটি বড় পরিবর্তনের পর আবার যাচাই করুন; আপডেটের সাথে প্রায়ই পুরোনো সমস্যা ফিরে আসে।</li>
</ul>

<h2>যা পেলেন তা কীভাবে লিখে রাখবেন</h2>
<p>প্রতিটি সমস্যার জন্য এক লাইনে লিখুন: পাতা, আপনি কী করেছিলেন, কী আশা করেছিলেন, কী ঘটেছে, স্ক্রিনশট, ডিভাইস ও ব্রাউজার, এবং কতটা গুরুতর। তাহলে যিনি ঠিক করবেন, তাঁকে আপনাকে কিছু জিজ্ঞেস করতে হবে না। <a href="/bn/articles/how-to-write-a-bug-report/">কীভাবে বাগ রিপোর্ট লিখবেন</a> লেখাটিতে একটি টেমপ্লেট আছে।</p>
""",
        "faq": [
            ("ওয়েবসাইট টেস্ট করতে কত সময় লাগে?", "৫ থেকে ১৫ পাতার একটি ছোট ব্যবসার সাইট ফোন ও কম্পিউটারে যত্ন নিয়ে যাচাই করতে সাধারণত এক থেকে দুই কর্মদিবস লাগে, ফলাফল লেখাসহ। লগ-ইনসহ অনলাইন শপ ও অ্যাপে বেশি সময় লাগে, কারণ প্রতিটি ধাপ শুরু থেকে শেষ পর্যন্ত করতে হয়।"),
            ("নিজের ওয়েবসাইট কি নিজে টেস্ট করা যায়?", "হ্যাঁ, করা উচিতও। তবে যিনি সাইট বানিয়েছেন তিনি সাধারণত চেনা পথেই চলেন। নতুন একজন টেস্টার, বা এমন কেউ যিনি সাইটটি আগে দেখেননি, ভিন্ন সমস্যা খুঁজে পান।"),
            ("কোনটি আগে ঠিক করা উচিত?", "যা দর্শককে প্রধান কাজ শেষ করতে বাধা দেয়: ভাঙা ফর্ম, পেমেন্টের ত্রুটি, ভুল দাম ও ভুল যোগাযোগের তথ্য। দেখতে কেমন লাগে সেই ধরনের সমস্যা পরে ঠিক করা যায়।"),
        ],
        "sources": [],
    },
})

# ---------------------------------------------------------------------------
ARTICLES.append({
    "slug": "how-to-write-a-bug-report",
    "date": "2026-11-24", "updated": "2026-11-24",
    "en": {
        "title": "How to write a bug report that gets fixed",
        "desc": "What a good bug report contains, a copy-ready template, and a simple severity scale so developers can fix problems without asking questions.",
        "short": "A good bug report lets someone who wasn't there see the problem for themselves. Give it a clear title, the page address, numbered steps to repeat it, what you expected and what actually happened, a screenshot or recording, the device and browser, and how serious it is. Report one problem per entry.",
        "body": """
<h2>Why most bug reports get ignored</h2>
<p>"The form doesn't work" is not something a developer can act on. Which form? On which page? What did you type? What happened instead? If the person fixing it has to come back with questions, the report waits in a queue. A report that answers those questions upfront usually gets fixed first.</p>

<h2>The eight parts of a good report</h2>
<dl class="defs">
  <div><dt>Title</dt><dd>What is broken and where, in one line. "Checkout: Pay button does nothing on iPhone Safari" beats "Payment bug".</dd></div>
  <div><dt>Page address</dt><dd>The full URL where it happens.</dd></div>
  <div><dt>Steps to repeat</dt><dd>Numbered steps from a clear starting point. Include what you typed or selected.</dd></div>
  <div><dt>Expected result</dt><dd>What should have happened.</dd></div>
  <div><dt>Actual result</dt><dd>What happened instead, including any error message word for word.</dd></div>
  <div><dt>Evidence</dt><dd>A screenshot with the problem area marked, or a short screen recording for anything that moves.</dd></div>
  <div><dt>Environment</dt><dd>Device, operating system, browser and version, and whether you were logged in.</dd></div>
  <div><dt>Severity</dt><dd>How much it hurts users (see the scale below).</dd></div>
</dl>

<h2>Template you can copy</h2>
<pre class="template"><code>Title:        [Page]: [what is wrong] on [device/browser]
Page:         https://
Steps:        1.
              2.
              3.
Expected:
Actual:
Evidence:     [screenshot / recording link]
Environment:  [device], [OS + version], [browser + version], logged in: yes/no
Severity:     High / Medium / Low
How often:    Every time / Sometimes (x of y tries)</code></pre>

<h2>A simple severity scale</h2>
<ul>
  <li><strong>High:</strong> stops people completing a main task (buying, signing up, contacting you), loses data, or shows wrong prices or legal information.</li>
  <li><strong>Medium:</strong> the task can be done, but it is confusing, slow, or needs a workaround; or a help page gives wrong directions.</li>
  <li><strong>Low:</strong> cosmetic or minor wording problems that do not stop anyone.</li>
</ul>
<p>Severity is about the effect on users. Priority (what gets fixed first) is the team's decision and can also depend on deadlines and effort.</p>

<h2>Good habits</h2>
<ul>
  <li>One problem per report. Two problems in one report means one of them gets forgotten.</li>
  <li>Try it twice before reporting, and say if it happens every time or only sometimes.</li>
  <li>Write the error message exactly; don't paraphrase it.</li>
  <li>Check whether it already has a report before adding a new one.</li>
  <li>Use test accounts and fake data in screenshots; never share real customers' details.</li>
  <li>When the fix is ready, check it again and close the report yourself.</li>
</ul>

<h2>Example</h2>
<p><strong>Title:</strong> Product page: price differs from cart price (৳2,450 vs ৳2,650)<br>
<strong>Steps:</strong> 1. Open the product page. 2. Note the price. 3. Tap "Add to cart". 4. Open the cart.<br>
<strong>Expected:</strong> Cart shows ৳2,450. <strong>Actual:</strong> Cart shows ৳2,650.<br>
<strong>Environment:</strong> Android 15, Chrome 131, not logged in. <strong>Severity:</strong> High. <strong>How often:</strong> Every time.</p>
<p>This example is illustrative. See more on our <a href="/sample-work/">sample work</a> page.</p>
""",
        "faq": [
            ("What is the difference between severity and priority?", "Severity describes how much a bug harms users. Priority is the order in which the team will fix bugs, which also depends on deadlines, effort and business needs. A low-severity typo on the home page can still get high priority."),
            ("Should I include a video or a screenshot?", "Use a screenshot for something you can see in one moment, such as wrong text. Use a short recording for anything that involves movement or several steps, such as a button that does nothing when tapped."),
            ("What if I can't make the bug happen again?", "Report it anyway, say it happened once, and include everything you remember: the time, the page, the device and what you were doing. Intermittent bugs are often the most important ones."),
        ],
        "sources": [],
    },
    "bn": {
        "title": "এমন বাগ রিপোর্ট কীভাবে লিখবেন যা ঠিক করা হয়",
        "desc": "একটি ভালো বাগ রিপোর্টে কী থাকে, কপি করার মতো টেমপ্লেট, এবং একটি সহজ গুরুত্ব-মাপকাঠি, যাতে ডেভেলপার প্রশ্ন না করেই সমস্যা ঠিক করতে পারেন।",
        "short": "ভালো বাগ রিপোর্ট এমন যে, যিনি সেখানে ছিলেন না তিনিও নিজে সমস্যাটি দেখতে পারেন। একটি স্পষ্ট শিরোনাম, পাতার ঠিকানা, আবার ঘটানোর ক্রমিক ধাপ, কী আশা করেছিলেন আর আসলে কী ঘটেছে, স্ক্রিনশট বা রেকর্ডিং, ডিভাইস ও ব্রাউজার, এবং কতটা গুরুতর — এসব দিন। প্রতিটি এন্ট্রিতে একটি সমস্যা।",
        "body": """
<h2>বেশিরভাগ বাগ রিপোর্ট কেন উপেক্ষিত হয়</h2>
<p>"ফর্ম কাজ করছে না" — এই কথায় ডেভেলপার কিছু করতে পারেন না। কোন ফর্ম? কোন পাতায়? কী লিখেছিলেন? বদলে কী ঘটেছে? যিনি ঠিক করবেন তাঁকে যদি প্রশ্ন নিয়ে ফিরে আসতে হয়, রিপোর্টটি সারিতে পড়ে থাকে। যে রিপোর্ট শুরুতেই এসব প্রশ্নের উত্তর দেয়, সেটি সাধারণত আগে ঠিক হয়।</p>

<h2>ভালো রিপোর্টের আটটি অংশ</h2>
<dl class="defs">
  <div><dt>শিরোনাম</dt><dd>কী ভেঙেছে এবং কোথায়, এক লাইনে। "চেকআউট: আইফোন সাফারিতে পে বাটনে কিছু হয় না" — "পেমেন্ট বাগ"-এর চেয়ে অনেক ভালো।</dd></div>
  <div><dt>পাতার ঠিকানা</dt><dd>যে পাতায় ঘটে তার পুরো URL।</dd></div>
  <div><dt>আবার ঘটানোর ধাপ</dt><dd>একটি স্পষ্ট শুরুর জায়গা থেকে ক্রমিক ধাপ। কী লিখেছেন বা বেছেছেন তা-ও দিন।</dd></div>
  <div><dt>প্রত্যাশিত ফল</dt><dd>কী হওয়ার কথা ছিল।</dd></div>
  <div><dt>আসল ফল</dt><dd>বদলে কী ঘটেছে, কোনো ত্রুটির বার্তা থাকলে হুবহু।</dd></div>
  <div><dt>প্রমাণ</dt><dd>সমস্যার জায়গা চিহ্নিত স্ক্রিনশট, অথবা নড়াচড়া আছে এমন কিছুর জন্য ছোট স্ক্রিন রেকর্ডিং।</dd></div>
  <div><dt>পরিবেশ</dt><dd>ডিভাইস, অপারেটিং সিস্টেম, ব্রাউজার ও সংস্করণ, এবং লগ-ইন অবস্থায় ছিলেন কি না।</dd></div>
  <div><dt>গুরুত্ব</dt><dd>ব্যবহারকারীর কতটা ক্ষতি হয় (নিচের মাপকাঠি দেখুন)।</dd></div>
</dl>

<h2>কপি করার মতো টেমপ্লেট</h2>
<pre class="template"><code>শিরোনাম:     [পাতা]: [কী ভুল] — [ডিভাইস/ব্রাউজার]
পাতা:        https://
ধাপ:         ১.
             ২.
             ৩.
প্রত্যাশিত:
আসল ফল:
প্রমাণ:      [স্ক্রিনশট / রেকর্ডিংয়ের লিংক]
পরিবেশ:      [ডিভাইস], [OS + সংস্করণ], [ব্রাউজার + সংস্করণ], লগ-ইন: হ্যাঁ/না
গুরুত্ব:      উচ্চ / মাঝারি / নিম্ন
কতবার:       প্রতিবার / মাঝে মাঝে (y বারের মধ্যে x বার)</code></pre>

<h2>একটি সহজ গুরুত্ব-মাপকাঠি</h2>
<ul>
  <li><strong>উচ্চ:</strong> মানুষকে প্রধান কাজ (কেনা, সাইন-আপ, যোগাযোগ) শেষ করতে বাধা দেয়, তথ্য হারায়, অথবা ভুল দাম বা আইনি তথ্য দেখায়।</li>
  <li><strong>মাঝারি:</strong> কাজটি করা যায়, কিন্তু বিভ্রান্তিকর, ধীর, বা ঘুরপথ লাগে; অথবা হেল্প পাতা ভুল নির্দেশনা দেয়।</li>
  <li><strong>নিম্ন:</strong> দেখতে কেমন লাগে বা ছোটখাটো লেখার সমস্যা, যা কাউকে আটকায় না।</li>
</ul>
<p>গুরুত্ব (severity) হলো ব্যবহারকারীর ওপর প্রভাব। অগ্রাধিকার (priority) — কোনটি আগে ঠিক হবে — সেটি টিমের সিদ্ধান্ত, যা সময়সীমা ও পরিশ্রমের ওপরও নির্ভর করে।</p>

<h2>ভালো অভ্যাস</h2>
<ul>
  <li>প্রতি রিপোর্টে একটি সমস্যা। এক রিপোর্টে দুটি থাকলে একটি ভুলে যাওয়া হয়।</li>
  <li>রিপোর্টের আগে দুবার চেষ্টা করুন, এবং জানান প্রতিবার ঘটে নাকি মাঝে মাঝে।</li>
  <li>ত্রুটির বার্তা হুবহু লিখুন; নিজের ভাষায় বদলাবেন না।</li>
  <li>নতুন রিপোর্ট দেওয়ার আগে দেখুন এটি আগেই রিপোর্ট হয়েছে কি না।</li>
  <li>স্ক্রিনশটে টেস্ট অ্যাকাউন্ট ও নকল ডেটা ব্যবহার করুন; আসল ক্রেতার তথ্য কখনো শেয়ার করবেন না।</li>
  <li>সমাধান তৈরি হলে আবার যাচাই করুন এবং নিজেই রিপোর্টটি বন্ধ করুন।</li>
</ul>

<h2>উদাহরণ</h2>
<p><strong>শিরোনাম:</strong> প্রোডাক্ট পাতা: দাম কার্টের দামের সাথে মেলে না (৳২,৪৫০ বনাম ৳২,৬৫০)<br>
<strong>ধাপ:</strong> ১. প্রোডাক্ট পাতা খুলুন। ২. দাম দেখে রাখুন। ৩. "কার্টে যোগ করুন" চাপুন। ৪. কার্ট খুলুন।<br>
<strong>প্রত্যাশিত:</strong> কার্টে ৳২,৪৫০। <strong>আসল ফল:</strong> কার্টে ৳২,৬৫০।<br>
<strong>পরিবেশ:</strong> অ্যান্ড্রয়েড ১৫, ক্রোম ১৩১, লগ-ইন নয়। <strong>গুরুত্ব:</strong> উচ্চ। <strong>কতবার:</strong> প্রতিবার।</p>
<p>এই উদাহরণটি বোঝানোর জন্য বানানো। আরও দেখুন আমাদের <a href="/bn/sample-work/">কাজের নমুনা</a> পাতায়।</p>
""",
        "faq": [
            ("গুরুত্ব (severity) আর অগ্রাধিকার (priority)-এর পার্থক্য কী?", "গুরুত্ব বোঝায় একটি বাগ ব্যবহারকারীর কতটা ক্ষতি করে। অগ্রাধিকার হলো টিম কোন ক্রমে বাগ ঠিক করবে, যা সময়সীমা, পরিশ্রম ও ব্যবসার প্রয়োজনের ওপরও নির্ভর করে। হোম পাতার একটি ছোট বানান ভুলও উচ্চ অগ্রাধিকার পেতে পারে।"),
            ("ভিডিও দেব নাকি স্ক্রিনশট?", "এক মুহূর্তে দেখা যায় এমন কিছুর জন্য স্ক্রিনশট দিন, যেমন ভুল লেখা। নড়াচড়া বা কয়েকটি ধাপ আছে এমন কিছুর জন্য ছোট রেকর্ডিং দিন, যেমন এমন বাটন যা চাপলে কিছু হয় না।"),
            ("বাগটি যদি আবার ঘটাতে না পারি?", "তবুও রিপোর্ট করুন, জানান একবার ঘটেছে, এবং যা মনে আছে সব দিন: সময়, পাতা, ডিভাইস ও তখন কী করছিলেন। মাঝে মাঝে ঘটা বাগগুলো প্রায়ই সবচেয়ে গুরুত্বপূর্ণ।"),
        ],
        "sources": [],
    },
})

# ---------------------------------------------------------------------------
_AI_SOURCES = [
    ("Aggarwal et al., “GEO: Generative Engine Optimization”, KDD 2024 (arXiv 2311.09735)", "https://arxiv.org/abs/2311.09735"),
    ("Search Engine Land: AI citation data shows no universal top source (Tinuiti / Profound, Q1 2026)", "https://searchengineland.com/ai-citation-data-no-universal-top-source-brands-471285"),
    ("Cloudflare changelog: new AI traffic options (1 July 2026)", "https://developers.cloudflare.com/changelog/post/2026-07-01-ai-traffic-options/"),
]

ARTICLES.append({
    "slug": "how-ai-assistants-choose-sources",
    "date": "2026-11-24", "updated": "2026-11-24",
    "en": {
        "title": "How AI assistants choose which websites to cite: what the research says",
        "desc": "What research and 2026 citation data say about how ChatGPT, Perplexity, Gemini and Google AI features pick sources, and practical steps to make your pages easier to cite.",
        "short": "AI assistants that search the web pick pages they can reach, understand quickly and trust. Research found that adding sources, statistics and quotations made content up to about 40% more visible in AI answers, while keyword stuffing made it worse. Which sites get cited also differs a lot between ChatGPT, Perplexity, Gemini and Google's AI features. First make sure AI crawlers are not blocked, then write clear pages that answer one question well.",
        "body": """
<h2>How an AI answer finds its sources</h2>
<p>When an assistant answers a question about something current, it usually searches the web, reads a handful of pages and writes a summary, often with links to the pages it used. Your page can only be one of those links if three things are true: the assistant's crawler can reach it, the page plainly answers the question, and it looks more reliable than the other candidates.</p>

<h2>What the research found</h2>
<p>A study by researchers from Princeton and other institutions, published at the KDD 2024 conference, tested ways of rewriting web content and measured how visible it became inside AI-generated answers. Their headline result: optimisation "can boost visibility by up to 40%" (Aggarwal et al.). On their benchmark, compared with unchanged text:</p>
<div class="table-wrap" tabindex="0"><table>
<thead><tr><th scope="col">Change to the text</th><th scope="col">Effect on visibility (word-count measure)</th></tr></thead>
<tbody>
<tr><td>Adding relevant quotations</td><td>about +41%</td></tr>
<tr><td>Adding statistics</td><td>about +31%</td></tr>
<tr><td>Citing sources</td><td>about +28%</td></tr>
<tr><td>Improving fluency (clearer, smoother writing)</td><td>about +28%</td></tr>
<tr><td>Keyword stuffing</td><td>about −8% (worse)</td></tr>
</tbody></table></div>
<p class="small">Percentages calculated from the paper's Table 1 against its no-change baseline. These are results on a research benchmark, not a guarantee for any single site, and the authors note that results vary by subject area.</p>

<h2>Each assistant cites different sources</h2>
<p>A Q1 2026 study by Tinuiti and Profound, reported by Search Engine Land, tracked commercial questions across seven AI platforms and concluded there is "no universal top source." For example, Reddit made up 24% of Perplexity's citations in January 2026, more than 5% on ChatGPT, but only 0.1% on Google Gemini. The same report cites BrightEdge data that only about 17% of Google AI Overview citations overlap with page-one search results. In other words, ranking well in normal search helps, but it is not the whole story, and you should check each assistant separately.</p>

<h2>Make sure AI crawlers can reach your site</h2>
<p>Some hosting and security services can block AI crawlers. Cloudflare, for example, now lets site owners set separate rules for search, agent and training bots; for domains added from 15 September 2026, training and agent bots are blocked by default on pages that show ads, while search bots stay allowed. If you want to be cited, check that the search and answer crawlers you care about are allowed in your hosting settings and in <code>robots.txt</code>.</p>

<h2>Practical steps</h2>
<ul>
  <li><strong>Answer one question per page</strong>, and give the short answer in the first paragraph.</li>
  <li><strong>Back claims with numbers and named sources</strong>, and link to them.</li>
  <li><strong>Use plain headings, lists and tables</strong> so each part makes sense on its own.</li>
  <li><strong>Show who wrote it and when</strong>, and update the date when you revise it.</li>
  <li><strong>Add structured data</strong> (for example Article and FAQ markup) so the page type is clear to machines.</li>
  <li><strong>Be consistent everywhere</strong>: the same company name, products and facts on your site, profiles and listings.</li>
  <li><strong>Earn mentions on other sites</strong> that the assistants already cite in your field, such as industry directories, reviews and genuine community discussions.</li>
  <li><strong>Check results by asking the assistants</strong> the questions your customers ask, and record which sites they cite. Ask several times: answers change from run to run.</li>
</ul>

<h2>What not to expect</h2>
<p>No one can guarantee that an assistant will cite a page. Answers vary between runs, between assistants and over time, and a new site with few links from elsewhere usually takes longer to be picked up. Treat AI visibility as a result of being genuinely useful and easy to read, not as a trick.</p>
""",
        "faq": [
            ("Does keyword stuffing help AI assistants find my page?", "No. In the KDD 2024 GEO study, keyword stuffing reduced visibility in AI answers by about 8% compared with unchanged text. Clear writing with sources and statistics performed far better."),
            ("Do I need to rank on Google to be cited by AI?", "It helps, but it isn't enough on its own. Data reported by Search Engine Land suggests only about 17% of Google AI Overview citations overlap with page-one results, and each AI platform favours different sources."),
            ("How can I check if AI assistants mention my site?", "Ask ChatGPT, Perplexity, Gemini and Google's AI features the questions your customers would ask, several times each, and note which sites they cite. Dedicated tracking tools can do this at scale."),
        ],
        "sources": _AI_SOURCES,
    },
    "bn": {
        "title": "এআই সহকারীরা কোন ওয়েবসাইট উদ্ধৃত করে, কীভাবে বাছাই করে: গবেষণা যা বলে",
        "desc": "ChatGPT, Perplexity, Gemini ও গুগলের এআই ফিচার কীভাবে উৎস বাছাই করে, সে বিষয়ে গবেষণা ও ২০২৬ সালের তথ্য, এবং আপনার পাতা উদ্ধৃত হওয়ার উপযোগী করার ব্যবহারিক ধাপ।",
        "short": "যে এআই সহকারীরা ওয়েবে খোঁজে, তারা এমন পাতা বাছাই করে যেখানে পৌঁছানো যায়, যা দ্রুত বোঝা যায় এবং যা বিশ্বাসযোগ্য। গবেষণায় দেখা গেছে, উৎস, পরিসংখ্যান ও উদ্ধৃতি যোগ করলে এআই উত্তরে কনটেন্টের দৃশ্যমানতা প্রায় ৪০% পর্যন্ত বাড়ে, আর কিওয়ার্ড ঠাসাঠাসি করলে কমে। কোন সাইট উদ্ধৃত হয় তা ChatGPT, Perplexity, Gemini ও গুগলের এআই ফিচারে অনেক আলাদা। আগে নিশ্চিত করুন এআই ক্রলার আটকানো নেই, তারপর এমন স্পষ্ট পাতা লিখুন যা একটি প্রশ্নের ভালো উত্তর দেয়।",
        "body": """
<h2>এআই উত্তর কীভাবে উৎস খুঁজে পায়</h2>
<p>সাম্প্রতিক কোনো বিষয়ে প্রশ্নের উত্তর দিতে সহকারী সাধারণত ওয়েবে খোঁজে, কয়েকটি পাতা পড়ে এবং একটি সারাংশ লেখে — প্রায়ই ব্যবহৃত পাতার লিংকসহ। আপনার পাতা সেই লিংকগুলোর একটি হতে পারে কেবল তখনই, যখন তিনটি শর্ত পূরণ হয়: সহকারীর ক্রলার পাতায় পৌঁছাতে পারে, পাতাটি স্পষ্টভাবে প্রশ্নের উত্তর দেয়, এবং অন্য প্রার্থীদের চেয়ে বেশি নির্ভরযোগ্য মনে হয়।</p>

<h2>গবেষণায় যা পাওয়া গেছে</h2>
<p>প্রিন্সটনসহ কয়েকটি প্রতিষ্ঠানের গবেষকদের একটি গবেষণা, যা KDD 2024 সম্মেলনে প্রকাশিত হয়, ওয়েব কনটেন্ট নতুন করে লেখার বিভিন্ন উপায় পরীক্ষা করে এবং এআই-তৈরি উত্তরের ভেতরে তা কতটা দৃশ্যমান হয় মাপে। তাদের প্রধান ফল: অপ্টিমাইজেশন দৃশ্যমানতা "৪০% পর্যন্ত বাড়াতে পারে" (Aggarwal et al.)। তাদের বেঞ্চমার্কে, অপরিবর্তিত লেখার তুলনায়:</p>
<div class="table-wrap" tabindex="0"><table>
<thead><tr><th scope="col">লেখায় পরিবর্তন</th><th scope="col">দৃশ্যমানতায় প্রভাব (শব্দ-গণনা মাপ)</th></tr></thead>
<tbody>
<tr><td>প্রাসঙ্গিক উদ্ধৃতি যোগ</td><td>প্রায় +৪১%</td></tr>
<tr><td>পরিসংখ্যান যোগ</td><td>প্রায় +৩১%</td></tr>
<tr><td>উৎস উল্লেখ</td><td>প্রায় +২৮%</td></tr>
<tr><td>সাবলীলতা বাড়ানো (আরও স্পষ্ট ও মসৃণ লেখা)</td><td>প্রায় +২৮%</td></tr>
<tr><td>কিওয়ার্ড ঠাসাঠাসি</td><td>প্রায় −৮% (খারাপ)</td></tr>
</tbody></table></div>
<p class="small">শতাংশগুলো গবেষণাপত্রের Table 1 থেকে, অপরিবর্তিত লেখার তুলনায় হিসাব করা। এগুলো একটি গবেষণা বেঞ্চমার্কের ফল, কোনো নির্দিষ্ট সাইটের নিশ্চয়তা নয়; লেখকেরা জানিয়েছেন বিষয়ভেদে ফল আলাদা হয়।</p>

<h2>প্রতিটি সহকারী ভিন্ন উৎস উদ্ধৃত করে</h2>
<p>Tinuiti ও Profound-এর ২০২৬ সালের প্রথম প্রান্তিকের একটি গবেষণা, যা Search Engine Land প্রকাশ করেছে, সাতটি এআই প্ল্যাটফর্মে বাণিজ্যিক প্রশ্ন পর্যবেক্ষণ করে সিদ্ধান্তে পৌঁছেছে যে "সবার জন্য এক সেরা উৎস নেই।" যেমন, জানুয়ারি ২০২৬-এ Perplexity-র উদ্ধৃতির ২৪% ছিল Reddit, ChatGPT-তে ৫%-এর বেশি, কিন্তু Google Gemini-তে মাত্র ০.১%। একই প্রতিবেদনে BrightEdge-এর তথ্য উল্লেখ আছে যে Google AI Overview-এর উদ্ধৃতির মাত্র প্রায় ১৭% সার্চের প্রথম পাতার ফলাফলের সাথে মেলে। অর্থাৎ সাধারণ সার্চে ভালো অবস্থান সাহায্য করে, কিন্তু সেটিই সব নয় — প্রতিটি সহকারী আলাদাভাবে যাচাই করা উচিত।</p>

<h2>নিশ্চিত করুন এআই ক্রলার আপনার সাইটে পৌঁছাতে পারে</h2>
<p>কিছু হোস্টিং ও নিরাপত্তা সেবা এআই ক্রলার আটকাতে পারে। যেমন Cloudflare এখন সাইটের মালিককে সার্চ, এজেন্ট ও ট্রেনিং বটের জন্য আলাদা নিয়ম ঠিক করতে দেয়; ১৫ সেপ্টেম্বর ২০২৬ থেকে যুক্ত হওয়া ডোমেইনে বিজ্ঞাপনযুক্ত পাতায় ট্রেনিং ও এজেন্ট বট ডিফল্টভাবে আটকানো থাকে, আর সার্চ বট অনুমোদিত থাকে। আপনি উদ্ধৃত হতে চাইলে দেখে নিন, আপনার কাঙ্ক্ষিত সার্চ ও উত্তর-ক্রলারগুলো হোস্টিং সেটিংস ও <code>robots.txt</code>-এ অনুমোদিত কি না।</p>

<h2>ব্যবহারিক ধাপ</h2>
<ul>
  <li><strong>প্রতি পাতায় একটি প্রশ্নের উত্তর দিন</strong>, এবং প্রথম অনুচ্ছেদেই সংক্ষিপ্ত উত্তর দিন।</li>
  <li><strong>দাবির পক্ষে সংখ্যা ও উৎসের নাম দিন</strong>, এবং লিংক যুক্ত করুন।</li>
  <li><strong>সহজ শিরোনাম, তালিকা ও টেবিল ব্যবহার করুন</strong>, যাতে প্রতিটি অংশ আলাদাভাবেও বোঝা যায়।</li>
  <li><strong>কে লিখেছেন ও কবে, তা দেখান</strong>, এবং হালনাগাদ করলে তারিখ বদলান।</li>
  <li><strong>স্ট্রাকচার্ড ডেটা যোগ করুন</strong> (যেমন Article ও FAQ মার্কআপ), যাতে যন্ত্রের কাছে পাতার ধরন স্পষ্ট হয়।</li>
  <li><strong>সব জায়গায় একই তথ্য রাখুন</strong>: সাইট, প্রোফাইল ও তালিকায় একই প্রতিষ্ঠানের নাম, প্রোডাক্ট ও তথ্য।</li>
  <li><strong>অন্য সাইটে উল্লেখ অর্জন করুন</strong>, যেগুলো আপনার ক্ষেত্রে সহকারীরা আগে থেকেই উদ্ধৃত করে — যেমন শিল্পভিত্তিক ডিরেক্টরি, রিভিউ ও আসল কমিউনিটি আলোচনা।</li>
  <li><strong>সহকারীদের প্রশ্ন করে ফল যাচাই করুন</strong> — আপনার ক্রেতারা যে প্রশ্ন করেন — এবং কোন সাইট উদ্ধৃত হয় লিখে রাখুন। কয়েকবার জিজ্ঞেস করুন: প্রতিবার উত্তর বদলায়।</li>
</ul>

<h2>যা আশা করবেন না</h2>
<p>কোনো সহকারী একটি পাতা উদ্ধৃত করবেই — এমন নিশ্চয়তা কেউ দিতে পারে না। উত্তর প্রতিবার, প্রতিটি সহকারীতে এবং সময়ের সাথে বদলায়, এবং অন্য সাইট থেকে কম লিংক থাকা নতুন সাইট সাধারণত দেরিতে নজরে আসে। এআই দৃশ্যমানতাকে কৌশল নয়, বরং সত্যিকারের উপকারী ও সহজপাঠ্য হওয়ার ফল হিসেবে দেখুন।</p>
""",
        "faq": [
            ("কিওয়ার্ড ঠাসাঠাসি কি এআই সহকারীকে আমার পাতা খুঁজে পেতে সাহায্য করে?", "না। KDD 2024-এর GEO গবেষণায় কিওয়ার্ড ঠাসাঠাসি অপরিবর্তিত লেখার তুলনায় এআই উত্তরে দৃশ্যমানতা প্রায় ৮% কমিয়েছে। উৎস ও পরিসংখ্যানসহ স্পষ্ট লেখা অনেক ভালো করেছে।"),
            ("এআই-এ উদ্ধৃত হতে কি গুগলে র‍্যাংক করা জরুরি?", "সাহায্য করে, কিন্তু একা যথেষ্ট নয়। Search Engine Land-এ প্রকাশিত তথ্য অনুযায়ী Google AI Overview-এর উদ্ধৃতির মাত্র প্রায় ১৭% প্রথম পাতার ফলাফলের সাথে মেলে, এবং প্রতিটি এআই প্ল্যাটফর্ম ভিন্ন উৎস পছন্দ করে।"),
            ("এআই সহকারীরা আমার সাইটের কথা বলে কি না কীভাবে দেখব?", "ChatGPT, Perplexity, Gemini ও গুগলের এআই ফিচারকে আপনার ক্রেতাদের প্রশ্নগুলো কয়েকবার করে জিজ্ঞেস করুন, এবং কোন সাইট উদ্ধৃত হয় লিখে রাখুন। বিশেষ ট্র্যাকিং টুল বড় পরিসরে এই কাজ করতে পারে।"),
        ],
        "sources": _AI_SOURCES,
    },
})
