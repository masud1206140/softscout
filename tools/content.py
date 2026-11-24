# Page content for softscout.support, English (en) and Bengali (bn).
# Edit text here, then run:  python3 tools/build.py

SITE = {
    "email": "contact@softscout.support",
    "domain": "https://softscout.support",
}

NAV = [  # (slug, en label, bn label)
    ("", "Home", "হোম"),
    ("services", "Services", "সেবাসমূহ"),
    ("process", "How we work", "কাজের ধাপ"),
    ("sample-work", "Sample work", "কাজের নমুনা"),
    ("about", "About", "আমাদের সম্পর্কে"),
    ("contact", "Contact", "যোগাযোগ"),
]

UI = {
    "en": {
        "menu": "Menu",
        "close": "Close menu",
        "skip": "Skip to content",
        "lang_name": "বাংলা",
        "lang_label": "Read this page in Bengali",
        "email_us": "Email us",
        "footer": "SoftScout — website testing and marketing support.",
        "nf_title": "Page not found",
        "nf_body": "This address doesn't match any page on softscout.support. Check the spelling, or go to the home page.",
        "nf_cta": "Go to the home page",
    },
    "bn": {
        "menu": "মেনু",
        "close": "মেনু বন্ধ করুন",
        "skip": "মূল লেখায় যান",
        "lang_name": "English",
        "lang_label": "এই পাতাটি ইংরেজিতে পড়ুন",
        "email_us": "ইমেইল করুন",
        "footer": "সফটস্কাউট — ওয়েবসাইট টেস্টিং ও মার্কেটিং সহায়তা।",
        "nf_title": "পাতাটি পাওয়া যায়নি",
        "nf_body": "এই ঠিকানায় softscout.support-এ কোনো পাতা নেই। বানান দেখে নিন, অথবা হোম পাতায় যান।",
        "nf_cta": "হোম পাতায় যান",
    },
}

MAILTO_SUBJECT = {"en": "Website enquiry", "bn": "ওয়েবসাইট বিষয়ে জানতে চাই"}

# Sample inspection sheet shown on the home page (illustrative, not a real client)
SHEET = {
    "en": {
        "title": "Example findings: a product page",
        "note": "Illustrative example",
        "rows": [
            ("pass", "Page loads and is readable on a phone"),
            ("fail", "“Buy now” button is hidden behind the cookie banner"),
            ("warn", "Price on the page differs from the price in the cart"),
            ("fail", "Help guide names a menu that no longer exists"),
            ("pass", "Contact form sends and the reply arrives"),
        ],
        "legend": {"pass": "Works", "fail": "Broken", "warn": "Needs a look"},
    },
    "bn": {
        "title": "নমুনা ফলাফল: একটি প্রোডাক্ট পাতা",
        "note": "উদাহরণ মাত্র",
        "rows": [
            ("pass", "ফোনে পাতা খোলে এবং পড়া যায়"),
            ("fail", "কুকি ব্যানারের নিচে “এখনই কিনুন” বাটন ঢাকা পড়ে আছে"),
            ("warn", "পাতার দাম আর কার্টের দাম আলাদা"),
            ("fail", "হেল্প গাইডে এমন মেনুর নাম আছে যা এখন আর নেই"),
            ("pass", "যোগাযোগ ফর্ম পাঠানো যায় এবং উত্তর আসে"),
        ],
        "legend": {"pass": "ঠিক আছে", "fail": "ভুল", "warn": "দেখা দরকার"},
    },
}

PAGES = {}

# ---------------- HOME ----------------
PAGES[""] = {
    "en": {
        "title": "SoftScout — website testing and marketing support",
        "desc": "SoftScout tests websites and apps, finds the customers most likely to buy, and keeps your content and ads accurate and current.",
        "h1": "Find what's broken on your website. Then bring the right customers to it.",
        "lead": "SoftScout tests websites and apps the way your customers use them, works out who your best customers are, and keeps your content and ads accurate.",
        "cta": "Email us about your website",
        "cta2": "See our services",
        "body": """
<section class="block">
  <h2>What we do</h2>
  <dl class="svc-list">
    <div><dt><a href="services/#testing">Website and app testing</a></dt>
      <dd>We go through your pages, forms and sign-up or checkout steps on phones and computers, and record every problem with a screenshot and the steps to repeat it.</dd></div>
    <div><dt><a href="services/#customers">Customer research</a></dt>
      <dd>We find the types of companies and people most likely to buy from you, who makes the decision, and what makes them start looking.</dd></div>
    <div><dt><a href="services/#content">Content updates</a></dt>
      <dd>We find outdated claims, wrong names and missing information on your site, and rewrite it in plain language.</dd></div>
    <div><dt><a href="services/#ads">Content for ads</a></dt>
      <dd>We make sure each ad, its wording and the page it leads to tell the same story, so you pay for clicks that turn into enquiries.</dd></div>
  </dl>
</section>
<section class="block">
  <h2>How a job runs</h2>
  <ol class="steps">
    <li><strong>You tell us</strong> what you want checked or improved.</li>
    <li><strong>We agree</strong> the pages, the deadline and the price in writing.</li>
    <li><strong>We do the work</strong> on your live site and keep evidence.</li>
    <li><strong>You get a report</strong> with findings ranked by how much they matter.</li>
  </ol>
  <p><a href="process/">More about how we work</a></p>
</section>
""",
    },
    "bn": {
        "title": "সফটস্কাউট — ওয়েবসাইট টেস্টিং ও মার্কেটিং সহায়তা",
        "desc": "সফটস্কাউট ওয়েবসাইট ও অ্যাপ টেস্ট করে, সম্ভাব্য সেরা ক্রেতা খুঁজে বের করে, এবং আপনার কনটেন্ট ও বিজ্ঞাপন সঠিক ও হালনাগাদ রাখে।",
        "h1": "আপনার ওয়েবসাইটে কী ভুল আছে খুঁজে বের করুন। তারপর সঠিক ক্রেতাকে সেখানে আনুন।",
        "lead": "সফটস্কাউট আপনার ক্রেতারা যেভাবে ব্যবহার করেন সেভাবেই ওয়েবসাইট ও অ্যাপ টেস্ট করে, আপনার সেরা ক্রেতা কারা তা বের করে, এবং কনটেন্ট ও বিজ্ঞাপন সঠিক রাখে।",
        "cta": "আপনার ওয়েবসাইট নিয়ে ইমেইল করুন",
        "cta2": "আমাদের সেবাগুলো দেখুন",
        "body": """
<section class="block">
  <h2>আমরা যা করি</h2>
  <dl class="svc-list">
    <div><dt><a href="services/#testing">ওয়েবসাইট ও অ্যাপ টেস্টিং</a></dt>
      <dd>ফোন ও কম্পিউটারে আপনার পাতা, ফর্ম, সাইন-আপ বা চেকআউটের ধাপগুলো আমরা যাচাই করি, এবং প্রতিটি সমস্যা স্ক্রিনশট ও পুনরায় ঘটানোর ধাপসহ লিখে রাখি।</dd></div>
    <div><dt><a href="services/#customers">ক্রেতা গবেষণা</a></dt>
      <dd>কোন ধরনের প্রতিষ্ঠান ও মানুষ আপনার কাছ থেকে কেনার সম্ভাবনা বেশি, সিদ্ধান্ত কে নেন, এবং কী কারণে তাঁরা খোঁজা শুরু করেন — আমরা তা বের করি।</dd></div>
    <div><dt><a href="services/#content">কনটেন্ট হালনাগাদ</a></dt>
      <dd>আপনার সাইটে পুরোনো দাবি, ভুল নাম ও অনুপস্থিত তথ্য খুঁজে বের করে আমরা সহজ ভাষায় নতুন করে লিখি।</dd></div>
    <div><dt><a href="services/#ads">বিজ্ঞাপনের কনটেন্ট</a></dt>
      <dd>বিজ্ঞাপন, তার লেখা এবং যে পাতায় নিয়ে যায় — তিনটি যেন একই কথা বলে, যাতে আপনি এমন ক্লিকের জন্য টাকা দেন যা সত্যিকারের অনুসন্ধানে পরিণত হয়।</dd></div>
  </dl>
</section>
<section class="block">
  <h2>একটি কাজ যেভাবে চলে</h2>
  <ol class="steps">
    <li><strong>আপনি জানান</strong> কী যাচাই বা উন্নত করতে চান।</li>
    <li><strong>আমরা লিখিতভাবে ঠিক করি</strong> কোন পাতা, কবে শেষ এবং খরচ কত।</li>
    <li><strong>আমরা কাজ করি</strong> আপনার লাইভ সাইটে, প্রমাণসহ।</li>
    <li><strong>আপনি রিপোর্ট পান</strong> — গুরুত্ব অনুযায়ী সাজানো ফলাফলসহ।</li>
  </ol>
  <p><a href="process/">আমাদের কাজের ধাপ সম্পর্কে আরও জানুন</a></p>
</section>
""",
    },
}

# ---------------- SERVICES ----------------
PAGES["services"] = {
    "en": {
        "title": "Services — SoftScout",
        "desc": "Website and app testing, customer research, content updates and content for ads.",
        "h1": "Services",
        "lead": "Pick one service or combine them. Every job starts with a written scope, so you know what you will get before we begin.",
        "body": """
<section class="block svc" id="testing">
  <h2>Website and app testing</h2>
  <p>We use your site the way a new customer would and write down everything that gets in their way.</p>
  <h3>What we check</h3>
  <ul>
    <li>Links, buttons, forms, sign-up, log-in and checkout steps</li>
    <li>Phones, tablets and computers, in the common browsers</li>
    <li>Whether the text, prices and product details are correct</li>
    <li>Whether help pages and guides match what is actually on screen</li>
    <li>Basic speed and accessibility problems that stop people using the page</li>
  </ul>
  <h3>What you get</h3>
  <p>An issue log (spreadsheet) with each problem's page, how serious it is, what we saw, the steps to repeat it, a screenshot, and a suggested fix. After you fix things, we check again.</p>
</section>
<section class="block svc" id="customers">
  <h2>Customer research</h2>
  <p>We work out who is most likely to buy from you, so your marketing talks to the right people.</p>
  <ul>
    <li>A short profile of your best-fit customers: industry, size, region</li>
    <li>The job titles that decide and the ones that use the product</li>
    <li>Signs that a company is ready to buy now</li>
    <li>A starting list of target companies, if you need one</li>
  </ul>
</section>
<section class="block svc" id="content">
  <h2>Content updates</h2>
  <p>Websites go out of date quietly. We find what's wrong and fix the wording.</p>
  <ul>
    <li>A page-by-page review of outdated claims, wrong names, broken promises and gaps</li>
    <li>Rewrites in plain language that a first-time visitor understands</li>
    <li>Image descriptions and page details that help search engines and AI assistants read your site correctly</li>
    <li>Regular updates for news and blog pages, if you want them</li>
  </ul>
</section>
<section class="block svc" id="ads">
  <h2>Content for ads</h2>
  <p>An ad works when the ad, its wording and the page it opens all match what the person was looking for.</p>
  <ul>
    <li>Several versions of ad wording to test against each other</li>
    <li>Ideas for the search words and topics to target</li>
    <li>A check that the landing page answers the question the ad raised</li>
    <li>A simple plan for testing and reading the results</li>
  </ul>
  <p>This works for search ads, social media ads and the new ad formats inside AI assistants.</p>
</section>
""",
    },
    "bn": {
        "title": "সেবাসমূহ — সফটস্কাউট",
        "desc": "ওয়েবসাইট ও অ্যাপ টেস্টিং, ক্রেতা গবেষণা, কনটেন্ট হালনাগাদ এবং বিজ্ঞাপনের কনটেন্ট।",
        "h1": "সেবাসমূহ",
        "lead": "একটি সেবা নিন, অথবা কয়েকটি একসাথে। প্রতিটি কাজ লিখিত পরিধি দিয়ে শুরু হয়, তাই শুরুর আগেই জানবেন কী পাবেন।",
        "body": """
<section class="block svc" id="testing">
  <h2>ওয়েবসাইট ও অ্যাপ টেস্টিং</h2>
  <p>একজন নতুন ক্রেতা যেভাবে আপনার সাইট ব্যবহার করবেন, আমরা সেভাবেই ব্যবহার করি এবং তাঁর পথে যা বাধা হয় সব লিখে রাখি।</p>
  <h3>আমরা যা যাচাই করি</h3>
  <ul>
    <li>লিংক, বাটন, ফর্ম, সাইন-আপ, লগ-ইন ও চেকআউটের ধাপ</li>
    <li>ফোন, ট্যাবলেট ও কম্পিউটার, প্রচলিত ব্রাউজারগুলোতে</li>
    <li>লেখা, দাম ও প্রোডাক্টের তথ্য সঠিক কি না</li>
    <li>হেল্প পাতা ও গাইড আসল স্ক্রিনের সাথে মেলে কি না</li>
    <li>গতি ও অ্যাক্সেসিবিলিটির মৌলিক সমস্যা, যা মানুষকে পাতা ব্যবহারে বাধা দেয়</li>
  </ul>
  <h3>আপনি যা পাবেন</h3>
  <p>একটি ইস্যু লগ (স্প্রেডশিট) — প্রতিটি সমস্যার পাতা, কতটা গুরুতর, আমরা কী দেখেছি, পুনরায় ঘটানোর ধাপ, স্ক্রিনশট ও সমাধানের পরামর্শসহ। আপনি ঠিক করার পর আমরা আবার যাচাই করি।</p>
</section>
<section class="block svc" id="customers">
  <h2>ক্রেতা গবেষণা</h2>
  <p>কারা আপনার কাছ থেকে কেনার সম্ভাবনা সবচেয়ে বেশি, আমরা তা বের করি — যাতে আপনার মার্কেটিং সঠিক মানুষের সাথে কথা বলে।</p>
  <ul>
    <li>আপনার সবচেয়ে উপযুক্ত ক্রেতাদের সংক্ষিপ্ত পরিচিতি: শিল্প, আকার, অঞ্চল</li>
    <li>কোন পদের মানুষ সিদ্ধান্ত নেন এবং কারা প্রোডাক্ট ব্যবহার করেন</li>
    <li>কোন লক্ষণ দেখে বোঝা যায় একটি প্রতিষ্ঠান এখনই কিনতে প্রস্তুত</li>
    <li>প্রয়োজনে লক্ষ্য প্রতিষ্ঠানগুলোর একটি প্রাথমিক তালিকা</li>
  </ul>
</section>
<section class="block svc" id="content">
  <h2>কনটেন্ট হালনাগাদ</h2>
  <p>ওয়েবসাইট নীরবে পুরোনো হয়ে যায়। কী ভুল আছে আমরা খুঁজে বের করি এবং লেখা ঠিক করি।</p>
  <ul>
    <li>প্রতিটি পাতা ধরে পুরোনো দাবি, ভুল নাম, রক্ষা না হওয়া প্রতিশ্রুতি ও ঘাটতির পর্যালোচনা</li>
    <li>এমন সহজ ভাষায় নতুন লেখা, যা প্রথমবারের দর্শকও বোঝেন</li>
    <li>ছবির বর্ণনা ও পাতার তথ্য, যা সার্চ ইঞ্জিন ও এআই সহকারীকে আপনার সাইট সঠিকভাবে পড়তে সাহায্য করে</li>
    <li>চাইলে নিউজ ও ব্লগ পাতার নিয়মিত হালনাগাদ</li>
  </ul>
</section>
<section class="block svc" id="ads">
  <h2>বিজ্ঞাপনের কনটেন্ট</h2>
  <p>বিজ্ঞাপন তখনই কাজ করে, যখন বিজ্ঞাপন, তার লেখা এবং যে পাতা খোলে — তিনটিই মানুষ যা খুঁজছিলেন তার সাথে মেলে।</p>
  <ul>
    <li>পরস্পরের সাথে তুলনা করে পরীক্ষার জন্য বিজ্ঞাপনের কয়েকটি সংস্করণ</li>
    <li>কোন সার্চ শব্দ ও বিষয় লক্ষ্য করবেন তার ধারণা</li>
    <li>বিজ্ঞাপন যে প্রশ্ন তুলেছে, ল্যান্ডিং পাতা তার উত্তর দেয় কি না তা যাচাই</li>
    <li>পরীক্ষা চালানো ও ফলাফল বোঝার একটি সহজ পরিকল্পনা</li>
  </ul>
  <p>এটি সার্চ বিজ্ঞাপন, সোশ্যাল মিডিয়া বিজ্ঞাপন এবং এআই সহকারীর ভেতরের নতুন বিজ্ঞাপনের জন্য কাজ করে।</p>
</section>
""",
    },
}

# ---------------- PROCESS ----------------
PAGES["process"] = {
    "en": {
        "title": "How we work — SoftScout",
        "desc": "How a SoftScout job runs, what we need from you, and how we handle your data.",
        "h1": "How we work",
        "lead": "Clear steps, written scope and evidence for every finding.",
        "body": """
<section class="block">
  <ol class="steps steps-long">
    <li><strong>Brief.</strong> You tell us your website, your goal and your deadline. A short email is enough.</li>
    <li><strong>Scope.</strong> We reply with the pages or tasks we will cover, what you will receive, the delivery date and the price. Work starts when you agree.</li>
    <li><strong>Work.</strong> We test or review your live site and record evidence: screenshots, steps and page addresses.</li>
    <li><strong>Report.</strong> You get the report in a spreadsheet or document, with the most serious problems first.</li>
    <li><strong>Re-check.</strong> When you have made fixes, we check those items again and update the report.</li>
  </ol>
</section>
<section class="block">
  <h2>What we need from you</h2>
  <ul>
    <li>Your website or app address</li>
    <li>What matters most: a page, a flow, a product or a campaign</li>
    <li>A test account, if parts of the site need a log-in</li>
    <li>One person we can ask questions</li>
  </ul>
</section>
<section class="block">
  <h2>How we handle your data</h2>
  <ul>
    <li>We use test accounts and test data, not real customer details.</li>
    <li>We don't share your reports or findings with anyone else.</li>
    <li>We don't show your work as an example without your written permission.</li>
    <li>When the job ends, you can remove our access.</li>
  </ul>
</section>
""",
    },
    "bn": {
        "title": "কাজের ধাপ — সফটস্কাউট",
        "desc": "সফটস্কাউটের একটি কাজ কীভাবে চলে, আপনার কাছ থেকে কী দরকার, এবং আমরা আপনার তথ্য কীভাবে রাখি।",
        "h1": "আমাদের কাজের ধাপ",
        "lead": "স্পষ্ট ধাপ, লিখিত পরিধি, এবং প্রতিটি ফলাফলের প্রমাণ।",
        "body": """
<section class="block">
  <ol class="steps steps-long">
    <li><strong>জানানো।</strong> আপনার ওয়েবসাইট, লক্ষ্য ও সময়সীমা আমাদের জানান। একটি ছোট ইমেইলই যথেষ্ট।</li>
    <li><strong>পরিধি।</strong> আমরা জানাই কোন পাতা বা কাজ করব, আপনি কী পাবেন, কবে দেব এবং খরচ কত। আপনি রাজি হলে কাজ শুরু হয়।</li>
    <li><strong>কাজ।</strong> আমরা আপনার লাইভ সাইট টেস্ট বা পর্যালোচনা করি এবং প্রমাণ রাখি: স্ক্রিনশট, ধাপ ও পাতার ঠিকানা।</li>
    <li><strong>রিপোর্ট।</strong> আপনি স্প্রেডশিট বা ডকুমেন্টে রিপোর্ট পান, সবচেয়ে গুরুতর সমস্যাগুলো সবার আগে।</li>
    <li><strong>পুনঃযাচাই।</strong> আপনি সমস্যা ঠিক করার পর আমরা সেগুলো আবার যাচাই করে রিপোর্ট হালনাগাদ করি।</li>
  </ol>
</section>
<section class="block">
  <h2>আপনার কাছ থেকে যা দরকার</h2>
  <ul>
    <li>আপনার ওয়েবসাইট বা অ্যাপের ঠিকানা</li>
    <li>কোনটি সবচেয়ে গুরুত্বপূর্ণ: একটি পাতা, একটি ধাপ, একটি প্রোডাক্ট বা একটি ক্যাম্পেইন</li>
    <li>সাইটের কিছু অংশে লগ-ইন লাগলে একটি টেস্ট অ্যাকাউন্ট</li>
    <li>প্রশ্ন করার জন্য একজন যোগাযোগের মানুষ</li>
  </ul>
</section>
<section class="block">
  <h2>আমরা আপনার তথ্য যেভাবে রাখি</h2>
  <ul>
    <li>আমরা টেস্ট অ্যাকাউন্ট ও টেস্ট ডেটা ব্যবহার করি, আসল ক্রেতার তথ্য নয়।</li>
    <li>আপনার রিপোর্ট বা ফলাফল আমরা অন্য কারও সাথে শেয়ার করি না।</li>
    <li>আপনার লিখিত অনুমতি ছাড়া আপনার কাজ উদাহরণ হিসেবে দেখাই না।</li>
    <li>কাজ শেষ হলে আপনি আমাদের অ্যাক্সেস সরিয়ে নিতে পারেন।</li>
  </ul>
</section>
""",
    },
}

# ---------------- SAMPLE WORK ----------------
SAMPLE_ROWS = {
    "en": [
        ("SS-01", "Checkout", "High", "Payment button does nothing on iPhone Safari.", "Fix the script error shown in the browser console; retest on iOS."),
        ("SS-02", "Product page", "High", "Price is ৳2,450 on the page but ৳2,650 in the cart.", "Use one price source for both."),
        ("SS-03", "Help guide", "Medium", "Guide says “Settings → Export”; the menu is now called “Reports”.", "Update the guide text and screenshot."),
        ("SS-04", "Home", "Low", "Image description names the wrong product.", "Rewrite the image description."),
    ],
    "bn": [
        ("SS-01", "চেকআউট", "উচ্চ", "আইফোনের সাফারিতে পেমেন্ট বাটনে চাপলে কিছু হয় না।", "ব্রাউজার কনসোলে দেখানো স্ক্রিপ্ট ত্রুটি ঠিক করুন; iOS-এ আবার টেস্ট করুন।"),
        ("SS-02", "প্রোডাক্ট পাতা", "উচ্চ", "পাতায় দাম ৳২,৪৫০, কিন্তু কার্টে ৳২,৬৫০।", "দুই জায়গায় একই উৎস থেকে দাম নিন।"),
        ("SS-03", "হেল্প গাইড", "মাঝারি", "গাইডে লেখা “Settings → Export”; মেনুর নাম এখন “Reports”।", "গাইডের লেখা ও স্ক্রিনশট হালনাগাদ করুন।"),
        ("SS-04", "হোম", "নিম্ন", "ছবির বর্ণনায় ভুল প্রোডাক্টের নাম।", "ছবির বর্ণনা নতুন করে লিখুন।"),
    ],
}

def _sample_table(lang):
    h = {"en": ("ID", "Page", "Severity", "What we saw", "Suggested fix"),
         "bn": ("আইডি", "পাতা", "গুরুত্ব", "আমরা যা দেখেছি", "সমাধানের পরামর্শ")}[lang]
    sev_class = {"High": "high", "Medium": "med", "Low": "low", "উচ্চ": "high", "মাঝারি": "med", "নিম্ন": "low"}
    rows = "\n".join(
        f'<tr><td>{a}</td><td>{b}</td><td><span class="sev {sev_class[c]}">{c}</span></td><td>{d}</td><td>{e}</td></tr>'
        for a, b, c, d, e in SAMPLE_ROWS[lang])
    head = "".join(f"<th scope=\"col\">{x}</th>" for x in h)
    return f'<div class="table-wrap" tabindex="0"><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>'

PAGES["sample-work"] = {
    "en": {
        "title": "Sample work — SoftScout",
        "desc": "An illustrative example of a SoftScout issue log: what we saw, how serious it is, and how to fix it.",
        "h1": "Sample work",
        "lead": "This is what part of a testing report looks like. The website and findings below are made up for illustration; they are not from a real client.",
        "body": """
<section class="block">
  <h2>Example issue log</h2>
  {TABLE}
  <p class="small">In a real report, every row also has a screenshot, the page address, the device and browser, and the exact steps to repeat the problem.</p>
</section>
<section class="block">
  <h2>Other things we deliver</h2>
  <ul>
    <li>Page-by-page content review with suggested new wording</li>
    <li>Customer profile and buyer roles, in a short document</li>
    <li>Ad wording options and a testing plan</li>
  </ul>
  <p>Ask us for a fuller sample by email.</p>
</section>
""",
    },
    "bn": {
        "title": "কাজের নমুনা — সফটস্কাউট",
        "desc": "সফটস্কাউটের ইস্যু লগের একটি উদাহরণ: আমরা কী দেখেছি, কতটা গুরুতর, এবং কীভাবে ঠিক করবেন।",
        "h1": "কাজের নমুনা",
        "lead": "একটি টেস্টিং রিপোর্টের অংশ দেখতে এমন হয়। নিচের ওয়েবসাইট ও ফলাফল উদাহরণের জন্য বানানো; কোনো আসল ক্লায়েন্টের নয়।",
        "body": """
<section class="block">
  <h2>নমুনা ইস্যু লগ</h2>
  {TABLE}
  <p class="small">আসল রিপোর্টে প্রতিটি সারিতে স্ক্রিনশট, পাতার ঠিকানা, ডিভাইস ও ব্রাউজার, এবং সমস্যাটি আবার ঘটানোর সঠিক ধাপও থাকে।</p>
</section>
<section class="block">
  <h2>আমরা আর যা দিই</h2>
  <ul>
    <li>প্রস্তাবিত নতুন লেখাসহ প্রতিটি পাতার কনটেন্ট পর্যালোচনা</li>
    <li>ক্রেতার পরিচিতি ও সিদ্ধান্তগ্রহণকারীদের পদ, একটি ছোট ডকুমেন্টে</li>
    <li>বিজ্ঞাপনের লেখার কয়েকটি বিকল্প ও পরীক্ষার পরিকল্পনা</li>
  </ul>
  <p>আরও বিস্তারিত নমুনার জন্য আমাদের ইমেইল করুন।</p>
</section>
""",
    },
}
for _l in ("en", "bn"):
    PAGES["sample-work"][_l]["body"] = PAGES["sample-work"][_l]["body"].replace("{TABLE}", _sample_table(_l))

# ---------------- ABOUT ----------------
PAGES["about"] = {
    "en": {
        "title": "About — SoftScout",
        "desc": "SoftScout is a detail-focused website testing and marketing support service based in Dhaka, Bangladesh.",
        "h1": "About SoftScout",
        "lead": "SoftScout is a small, detail-focused service based in Dhaka, Bangladesh, working with clients anywhere by email and online calls.",
        "body": """
<section class="block">
  <p>We come from engineering, so we work from checklists, evidence and clear records. Every finding comes with what we saw and how to repeat it, so your team can act on it without a meeting.</p>
  <h2>What we care about</h2>
  <dl class="values">
    <div><dt>Evidence, not opinion</dt><dd>Each problem has a screenshot, the steps and the page address.</dd></div>
    <div><dt>Plain language</dt><dd>Reports and website text that a busy reader understands the first time.</dd></div>
    <div><dt>English and Bengali</dt><dd>We work and write in both languages.</dd></div>
  </dl>
</section>
""",
    },
    "bn": {
        "title": "আমাদের সম্পর্কে — সফটস্কাউট",
        "desc": "সফটস্কাউট ঢাকা, বাংলাদেশভিত্তিক একটি খুঁটিনাটিতে মনোযোগী ওয়েবসাইট টেস্টিং ও মার্কেটিং সহায়তা সেবা।",
        "h1": "সফটস্কাউট সম্পর্কে",
        "lead": "সফটস্কাউট ঢাকা, বাংলাদেশভিত্তিক একটি ছোট, খুঁটিনাটিতে মনোযোগী সেবা। ইমেইল ও অনলাইন কলের মাধ্যমে আমরা যেকোনো জায়গার ক্লায়েন্টের সাথে কাজ করি।",
        "body": """
<section class="block">
  <p>আমাদের পটভূমি প্রকৌশল, তাই আমরা চেকলিস্ট, প্রমাণ ও পরিষ্কার রেকর্ড ধরে কাজ করি। প্রতিটি ফলাফলের সাথে থাকে আমরা কী দেখেছি এবং কীভাবে আবার ঘটানো যায় — যাতে আপনার টিম মিটিং ছাড়াই কাজ শুরু করতে পারে।</p>
  <h2>আমরা যা গুরুত্ব দিই</h2>
  <dl class="values">
    <div><dt>মতামত নয়, প্রমাণ</dt><dd>প্রতিটি সমস্যার সাথে স্ক্রিনশট, ধাপ ও পাতার ঠিকানা।</dd></div>
    <div><dt>সহজ ভাষা</dt><dd>রিপোর্ট ও ওয়েবসাইটের লেখা, যা ব্যস্ত পাঠকও প্রথমবারেই বোঝেন।</dd></div>
    <div><dt>ইংরেজি ও বাংলা</dt><dd>আমরা দুই ভাষাতেই কাজ করি ও লিখি।</dd></div>
  </dl>
</section>
""",
    },
}

# ---------------- CONTACT ----------------
PAGES["contact"] = {
    "en": {
        "title": "Contact — SoftScout",
        "desc": "Email SoftScout at contact@softscout.support about testing your website or improving your content and ads.",
        "h1": "Contact",
        "lead": "Email us. Tell us your website and what you want checked or improved, and we will reply with a scope and a price.",
        "body": """
<section class="block contact-card">
  <p class="contact-email"><a href="mailto:{EMAIL}?subject={SUBJ}">{EMAIL}</a></p>
  <p><a class="btn" href="mailto:{EMAIL}?subject={SUBJ}">Write an email</a></p>
</section>
<section class="block">
  <h2>What to include</h2>
  <ul>
    <li>Your website or app address</li>
    <li>What you want: testing, customer research, content or ads</li>
    <li>Your deadline, if you have one</li>
    <li>Whether parts of the site need a log-in</li>
  </ul>
  <p class="small">We reply from {EMAIL}. If you don't see our reply, check your spam folder.</p>
</section>
""",
    },
    "bn": {
        "title": "যোগাযোগ — সফটস্কাউট",
        "desc": "ওয়েবসাইট টেস্টিং বা কনটেন্ট ও বিজ্ঞাপন উন্নত করতে সফটস্কাউটকে contact@softscout.support-এ ইমেইল করুন।",
        "h1": "যোগাযোগ",
        "lead": "আমাদের ইমেইল করুন। আপনার ওয়েবসাইট এবং কী যাচাই বা উন্নত করতে চান জানান — আমরা কাজের পরিধি ও খরচ জানিয়ে উত্তর দেব।",
        "body": """
<section class="block contact-card">
  <p class="contact-email"><a href="mailto:{EMAIL}?subject={SUBJ}">{EMAIL}</a></p>
  <p><a class="btn" href="mailto:{EMAIL}?subject={SUBJ}">ইমেইল লিখুন</a></p>
</section>
<section class="block">
  <h2>ইমেইলে যা লিখবেন</h2>
  <ul>
    <li>আপনার ওয়েবসাইট বা অ্যাপের ঠিকানা</li>
    <li>কী চান: টেস্টিং, ক্রেতা গবেষণা, কনটেন্ট নাকি বিজ্ঞাপন</li>
    <li>সময়সীমা থাকলে সেটি</li>
    <li>সাইটের কোনো অংশে লগ-ইন লাগে কি না</li>
  </ul>
  <p class="small">আমরা {EMAIL} থেকে উত্তর দিই। উত্তর না দেখলে স্প্যাম ফোল্ডার দেখে নিন।</p>
</section>
""",
    },
}
