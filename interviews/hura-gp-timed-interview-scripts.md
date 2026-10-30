# Timed interview scripts

Five run-of-show scripts, each timed to the minute and ranked so the first questions are the ones you cannot leave without. Your lines are in quotes and are verbatim; read them as written. Directions are in italics. Each block opens with a hook line that gives the interviewee something to push against; a question with a hook in front of it gets a story, a bare question gets a definition. If you run over, cut from the bottom of each block, never the top.

Total on-camera time: CTO 20 minutes, founder 20 minutes, broadcast lead 15 minutes, driver 10 minutes, robot operator 8 minutes. Seventy-three minutes of interview for a twenty-four minute episode, which is tight and right.

## CTO, 20 minutes

| Block | Minutes | Goal | Must get |
| --- | --- | --- | --- |
| A. The number | 0:00 to 4:00 | the end-to-end latency, three values, and how they measure it | the number in a full sentence |
| B. What breaks | 4:00 to 8:00 | link loss as a sequence, prediction and fairness, build or buy | the watchdog story |
| C. Distance | 8:00 to 12:00 | Stockholm, home connection or private 5G, the operator wish list | whether cross-border is real |
| D. Car to robot | 12:00 to 15:00 | what changes in the stack, the surprise, the humanoid hook | the bridge line, in their words |
| E. The chip story | 15:00 to 18:00 | memory prices, the queue, data as product or cost | one concrete cost number |
| F. Limits and close | 18:00 to 20:00 | honest limits, the demonstration ask, closer, rapid-fire | the admission |

*Before the camera rolls, thirty seconds, off the record:* "I built T-boxes for years. Talk to me like an engineer. If I get something wrong, say so on camera; that is the good part."

**A. The number, 0:00 to 4:00**

*Hook, to camera then to them:* "Vay drives real cars in Las Vegas at city speed, and their engineers talk about tens of milliseconds. Your cars go a lot faster than that."

1. "End to end, from the car's camera to the driver's eye and back to the steering: how many milliseconds? Best case, race-day typical, and the worst you can still race on."
    *Follow-up, always:* "How do you measure that? Not the spec, the measurement."
2. "Where do those milliseconds go: encode, radio, transit, decode, screen? Which one did you fight hardest?"
    *Follow-up if they name one:* "What did it cost you to win that fight? Months, money, a redesign?"

**B. What breaks, 4:00 to 8:00**

*Hook:* "A T-box fails safe by doing nothing. Your box cannot do nothing at sixty kilometres an hour."

3. "The link drops at sixty kilometres an hour on the straight. What happens in the next two hundred milliseconds, in order?"
    *Follow-up:* "Has it happened in a race? Tell me about that one."
4. "Does the driver see where the car is, or where it will be? If you predict, is that an assist the referee should know about?"
5. "Which parts did you build and which did you buy: the modem, the codec, the transport protocol, the control stack, the box itself?"
    *Cut first if over time: question 5.*

**C. Distance, 8:00 to 12:00**

*Hook:* "Einride drove a truck in Sweden from Barcelona in 2019. Ericsson and Vay did Berlin from Barcelona in 2023 and said the video never went over two hundred milliseconds."

6. "Shanghai to Stockholm is about a hundred and sixty milliseconds there and back on today's internet, double what you quote for the track. Have you driven across a border yet? What was the number, and what broke?"
    *If not yet:* "If we put a driver in Stockholm during this shoot, what would you need from me by Monday?"
7. "Do you need the telecom operator's cooperation, private 5G, slicing, edge computing, or does this run on a home connection? Which one does the final run on?"
8. "If Ericsson's or Huawei's 5G team called tomorrow, what would you ask them for?"
    *Cut first if over time: question 8.*

**D. Car to robot, 12:00 to 15:00**

*Hook:* "Beijing ran six hundred and sixty-six teams of humanoids in August, and every operator was standing in the venue with a controller."

9. "When the far end is a humanoid instead of a car, what changes in the stack? Hands, balance, more cameras, less speed?"
10. "After the first cross-country robot run, what did the operator on the other end tell you that you did not expect?"
11. "Which humanoid will be on your track first, and will it be driven from another country?"
    *Cut first if over time: question 11.*

**E. The chip story, 15:00 to 18:00**

*Hook:* "Samsung has reportedly raised memory prices by up to sixty percent since September, and SK Hynix says supply stays tight for three more years."

12. "Your cockpits, your edge servers and your Ro-boxes all carry memory. What has the AI boom done to the cost of building one car and one cockpit?"
    *Follow-up:* "Give me the number. Last year versus this year, one cockpit."
13. "When SK Hynix and Samsung are selling every chip to Nvidia's customers, where does a Shanghai sports-technology company stand in the queue? Do you buy Chinese memory, CXMT or YMTC, and does it work?"
14. "Every race produces synchronised video, control inputs and car state. Storage is exactly the thing that got expensive this year. Is your data a product, or a cost?"
    *Cut first if over time: question 14.*

**F. Limits and close, 18:00 to 20:00**

15. "What can this not do yet that people assume it can?"
16. "What is the one thing that, if it broke on race day, would end the company?"
17. "Can you put the latency on the screen, live, while I drive a lap?"
    *Rapid-fire, thirty seconds, keep rolling:* "Short answers. Nvidia or Huawei: whose chips are in the box? If DRAM doubles again, what do you cut first? Your latency, in one word. One number everyone should remember from today."

*Held back, use only if a block runs short:* "Someone on the internet wants to take over a car mid-race. How do you stop them?" and "DeepSeek proved China can do more with fewer chips. Is there a DeepSeek move in teleoperation: more with less bandwidth, cheaper hardware, smaller models?"

## Founder, 20 minutes

| Block | Minutes | Goal | Must get |
| --- | --- | --- | --- |
| A. Origin and definition | 0:00 to 4:00 | the first remote drive, the one-sentence definition | the definition, in their words |
| B. Stakes and fairness | 4:00 to 8:00 | the crash, who pays, the latency rule | the fairness answer |
| C. The world | 8:00 to 12:00 | the Stockholm driver, the category, the sceptic | the sceptic answered |
| D. Robots and the bet | 12:00 to 16:00 | why robots under a racing brand, Nvidia's story, the squeeze | cars are the test, robots are the business |
| E. Money and close | 16:00 to 20:00 | where the money comes from, 2030, novelty closer, rapid-fire | the novelty answer |

*Before the camera rolls, off the record:* "I run a Chinese-founded studio in Sweden with a Western audience. I want this to be the film a European investor or an Ericsson engineer watches to understand what you have actually built, not the hype version. The sceptic's question stays in; that is what makes the rest believable."

**A. Origin and definition, 0:00 to 4:00**

1. "Tell me about the first time someone drove one of your cars from another city. Where were you standing, and what went wrong?"
    *Follow-up:* "And then what happened?"
2. "If I am a Formula 1 fan in London, what is HURA GP in one sentence? And if I am an esports fan in Seoul?"

**B. Stakes and fairness, 4:00 to 8:00**

*Hook:* "In a racing game, nothing is real. Here the crash is real and the driver still only sees a screen."

3. "What happens when a car crashes? Who pays, who fixes it, and does the driver see it?"
4. "Two drivers, one in Shanghai and one in Chengdu. The Chengdu driver has forty milliseconds more delay. Is that fair? What do you do about it?"
    *Follow-up:* "Would you slow the faster link down on purpose?"

**C. The world, 8:00 to 12:00**

*Hook:* "Finland tried this in 2019 and the company folded. Abu Dhabi races cars with no driver at all. You are the only ones doing it with a crowd watching."

5. "If a driver in Stockholm wanted to race in your next final, what would you need: technically, legally, commercially?"
6. "A sceptic in Europe will say: it is RC cars with a 5G sticker. What is your answer?"
7. "Is this esports, motorsport, or something that does not have a name yet? Who do you want to sanction you, the esports federations or the motorsport bodies?"
    *Cut first if over time: question 7.*

**D. Robots and the bet, 12:00 to 16:00**

*Hook:* "Nvidia calls this the decade of physical AI, and Jensen Huang says the next wave is robots."

8. "Why run robot competitions under a racing brand? What does a robot race teach you that a car race cannot?"
9. "Are you a customer of Nvidia's story or a competitor to it, since your robots have a human inside?"
10. "The memory makers say supply stays tight for three more years. If hardware gets dearer every quarter, do you end up owning more cars or fewer, and do drivers start bringing their own cockpits?"
    *Cut first if over time: question 10.*

**E. Money and close, 16:00 to 20:00**

11. "Where does the money come from today: tickets, sponsors, the telecom partners, technology licensing? Which one do you want it to be in three years?"
12. "Describe the final in 2030. Where are the cars, where are the drivers, and who is commentating?"
13. "If you take away the first-time novelty, why does anyone come back?"
    *Rapid-fire, thirty seconds:* "Short answers. Initial D or Drive to Survive? Who in the world would you most like to race? Would you put your champion against an AI driver, the way Abu Dhabi does? Finish the sentence: people think we are an RC car company, but..."

*Held back:* "What did you change after the last event that nobody noticed?" Use it the moment an answer turns into a press release.

## Broadcast lead, 15 minutes

| Block | Minutes | Goal | Must get |
| --- | --- | --- | --- |
| A. Going live | 0:00 to 4:00 | the last sixty seconds, two kinds of video | the milliseconds-versus-seconds line |
| B. The craft | 4:00 to 9:00 | cameras, Douyin versus venue, the counter, best and worst | what the audience sees that the driver does not |
| C. The audience | 9:00 to 13:00 | the non-gamer, Drive to Survive, one show or two, the numbers | three audience numbers |
| D. Close | 13:00 to 15:00 | the opening for the studio, the closer | the partnership answer |

**A. Going live, 0:00 to 4:00**

1. "Walk me through the last sixty seconds before you go live. What are you looking at?"
2. "There are two kinds of video in this building: what the driver sees and what the audience sees. How different are they, and why?"

**B. The craft, 4:00 to 9:00**

*Hook:* "Drone Racing League put the pilot's eyes on ESPN. You have the driver's eyes and the car's eyes at the same time."

3. "How many cameras, which ones are on the car, and which single shot could you not broadcast a race without?"
4. "What does a viewer on Douyin see that a person in the venue never sees?"
5. "Do you show the latency number to the audience? Why, or why not?"
    *If no:* "What if you did? What would the comments say?"
6. "The best moment you have broadcast so far, and the one you wish you had not."
    *Cut first if over time: question 3.*

**C. The audience, 9:00 to 13:00**

*Hook:* "Formula 1 took seventy years and a Netflix series to find a new audience."

7. "What is your Drive to Survive?"
8. "How do you make someone who does not play games care? Who is the main character of a race: the driver, the car or the engineer?"
9. "Same race, a viewer in Shanghai and a viewer in Stockholm. Do you produce one show or two? Commentary, language, pacing?"
10. "Peak concurrent viewers, average watch time, and the share who watched to the end."
    *Cut first if over time: question 9.*

**D. Close, 13:00 to 15:00**

11. "What could a Western studio do with your feed that you cannot do yourselves?"
12. "What moment are you still waiting to capture?"
    *Rapid-fire, twenty seconds:* "Real car or simulator: which is harder to broadcast? One number everyone should remember from today."

*Held back:* "Which broadcast did you copy when you started, and where did you stop copying?"

## Driver, 10 minutes

*Pick the driver who lost the final. Sit them in their cockpit if you can.*

| Block | Minutes | Goal |
| --- | --- | --- |
| A. The body | 0:00 to 4:00 | the delay as a feeling, the crash |
| B. The craft | 4:00 to 8:00 | three kinds of driving, last lap, training |
| C. Close | 8:00 to 10:00 | the European sim racer, parents, rapid-fire |

1. "What does the delay feel like? Describe it in your body, not in numbers."
2. "Where were you sitting when you lost the final? What was on the wall in front of you?"
3. "Your first crash in one of these: did you feel anything? What did you do in the next second?"
4. "You have raced in a game, with a handheld transmitter, and like this. Rank them by how hard they are, and by how real they feel."
5. "What do you do differently on the last lap? Does the delay change how you brake?"
6. "How do you train for this? Is there anything you do that a sim racer would laugh at?"
7. "A sim racer in Europe thinks this would be easy for them. What would you tell them?"
8. "What do you tell your parents you do?"
    *Rapid-fire, twenty seconds:* "Your latency, in one word. Motion seat: does it make you faster, or just happier? Who in the world would you most like to race?"

*Cut first if over time: questions 5 and 6.*

## Robot operator, 8 minutes

*If the robot programme is still at demo stage, interview whoever ran the test runs and say so in the cut.*

1. "What are you controlling, from where, and how far away is it?"
2. "What is the hardest thing a robot does by remote: walking, picking something up, or turning around?"
3. "Has the robot ever done something you did not ask it to?"
4. "When the robot falls, what do you feel?"
5. "You have driven the race car too. Which is harder, and why?"
6. "Do you think of yourself as a gamer, a pilot, or a robot trainer?"
    *Rapid-fire, fifteen seconds:* "Five years from now, what gets driven remotely that nobody expects? One word for the delay."

*Cut first if over time: question 6.*

## How the ranking was done

Three tests, in order. Does the answer give the episode something it cannot get elsewhere: the number, the definition, the fairness rule, the admission? Does the question carry a hook a Western viewer already recognises: Vay, Ericsson, Nvidia, Samsung, Drone Racing League, Drive to Survive? Does it produce a story, a number, a demonstration or an admission rather than an opinion? Questions that pass all three sit at the top of a block. Questions that pass one sit at the bottom and are the first to go. The trending questions are placed as the fifth block, not the first, because the chip story only works once the viewer already cares about the car.
