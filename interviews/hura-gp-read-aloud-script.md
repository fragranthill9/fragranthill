# Read-aloud script

Every line below is a line you say, in the order you say it. Nothing else is on the page. Headings and minute marks are for your eye only; do not read them. Narration at about 150 words a minute, questions slower, and a full stop of silence after each question.

## Narration, part 1

### Cold open

Eighty milliseconds. That is how long it takes this car to tell its driver where it is. The driver is ten kilometres away.

He felt nothing. He saw everything. Welcome to a sport where the referee is physics.

### Stakes

Every robot company in the world has the same unsolved problem. The machines are not ready to run themselves. So someone, somewhere, has to drive them, from far away, fast enough that nothing breaks. In Las Vegas a company called Vay does it with rental cars at city speed. In Shanghai, this company decided to do it at racing speed, in public, with a crowd watching. They call it HURA GP. I came to find out whether it is a sport, a technology demo, or the first look at how robots will actually be run.

### Piece to camera, beside the cockpit

I used to build the box that connects a car to the network. The T-box. It phones home, updates the software, unlocks the doors. What they have built is the same box pointed the other way: instead of the car talking to the cloud, a human in the cloud drives the car. The question is how many milliseconds that costs, and whether a human can live with it. I am about to find out.

### Bridge to the founder

In March, during the Formula 1 weekend, they ran their first season final a few hundred metres from the real circuit. The cars were on this track. The drivers were ten kilometres away. [The winner's name] won by [margin], which is less than the time it takes the video to reach his screen.

## Founder, 20 minutes

### Before the camera rolls

I run a Chinese-founded studio in Sweden with a Western audience. I want this to be the film a European investor or an Ericsson engineer watches to understand what you have actually built, not the hype version. The sceptic's question stays in; that is what makes the rest believable.

### A. Origin and definition, 0 to 4

Tell me about the first time someone drove one of your cars from another city. Where were you standing, and what went wrong?

And then what happened?

If I am a Formula 1 fan in London, what is HURA GP in one sentence? And if I am an esports fan in Seoul?

### B. Stakes and fairness, 4 to 8

In a racing game, nothing is real. Here the crash is real and the driver still only sees a screen.

What happens when a car crashes? Who pays, who fixes it, and does the driver see it?

Two drivers, one in Shanghai and one in Chengdu. The Chengdu driver has forty milliseconds more delay. Is that fair? What do you do about it?

Would you slow the faster link down on purpose?

### C. The world, 8 to 12

Finland tried this in 2019 and the company folded. Abu Dhabi races cars with no driver at all. You are the only ones doing it with a crowd watching.

If a driver in Stockholm wanted to race in your next final, what would you need: technically, legally, commercially?

A sceptic in Europe will say: it is RC cars with a 5G sticker. What is your answer?

Is this esports, motorsport, or something that does not have a name yet? Who do you want to sanction you, the esports federations or the motorsport bodies?

### D. Robots and the bet, 12 to 16

Nvidia calls this the decade of physical AI, and Jensen Huang says the next wave is robots.

Why run robot competitions under a racing brand? What does a robot race teach you that a car race cannot?

Are you a customer of Nvidia's story or a competitor to it, since your robots have a human inside?

The memory makers say supply stays tight for three more years. If hardware gets dearer every quarter, do you end up owning more cars or fewer, and do drivers start bringing their own cockpits?

### E. Money and close, 16 to 20

Where does the money come from today: tickets, sponsors, the telecom partners, technology licensing? Which one do you want it to be in three years?

Describe the final in 2030. Where are the cars, where are the drivers, and who is commentating?

If you take away the first-time novelty, why does anyone come back?

Short answers, first thing that comes to mind. Initial D or Drive to Survive? Who in the world would you most like to race? Would you put your champion against an AI driver, the way Abu Dhabi does? Finish the sentence: people think we are an RC car company, but...

### Held back

What did you change after the last event that nobody noticed?

## Narration, part 2

### Bridge to the CTO

Here is the whole trick in one picture. Control goes out, video comes back, and the race lives in the round trip. The company says that round trip is under eighty milliseconds. I wanted to know where every one of them goes.

## CTO, 20 minutes

### Before the camera rolls

I built T-boxes for years. Talk to me like an engineer. If I get something wrong, say so on camera; that is the good part.

### A. The number, 0 to 4

Vay drives real cars in Las Vegas at city speed, and their engineers talk about tens of milliseconds. Your cars go a lot faster than that.

End to end, from the car's camera to the driver's eye and back to the steering: how many milliseconds? Best case, race-day typical, and the worst you can still race on.

How do you measure that? Not the spec, the measurement.

Where do those milliseconds go: encode, radio, transit, decode, screen? Which one did you fight hardest?

What did it cost you to win that fight? Months, money, a redesign?

### B. What breaks, 4 to 8

A T-box fails safe by doing nothing. Your box cannot do nothing at sixty kilometres an hour.

The link drops at sixty kilometres an hour on the straight. What happens in the next two hundred milliseconds, in order?

Has it happened in a race? Tell me about that one.

Does the driver see where the car is, or where it will be? If you predict, is that an assist the referee should know about?

Which parts did you build and which did you buy: the modem, the codec, the transport protocol, the control stack, the box itself?

### C. Distance, 8 to 12

Einride drove a truck in Sweden from Barcelona in 2019. Ericsson and Vay did Berlin from Barcelona in 2023 and said the video never went over two hundred milliseconds.

Shanghai to Stockholm is about a hundred and sixty milliseconds there and back on today's internet, double what you quote for the track. Have you driven across a border yet? What was the number, and what broke?

If we put a driver in Stockholm during this shoot, what would you need from me by Monday?

Do you need the telecom operator's cooperation, private 5G, slicing, edge computing, or does this run on a home connection? Which one does the final run on?

If Ericsson's or Huawei's 5G team called tomorrow, what would you ask them for?

### D. Car to robot, 12 to 15

Beijing ran six hundred and sixty-six teams of humanoids in August, and every operator was standing in the venue with a controller.

When the far end is a humanoid instead of a car, what changes in the stack? Hands, balance, more cameras, less speed?

After the first cross-country robot run, what did the operator on the other end tell you that you did not expect?

Which humanoid will be on your track first, and will it be driven from another country?

### E. The chip story, 15 to 18

Samsung has reportedly raised memory prices by up to sixty percent since September, and SK Hynix says supply stays tight for three more years.

Your cockpits, your edge servers and your Ro-boxes all carry memory. What has the AI boom done to the cost of building one car and one cockpit?

Give me the number. Last year versus this year, one cockpit.

When SK Hynix and Samsung are selling every chip to Nvidia's customers, where does a Shanghai sports-technology company stand in the queue? Do you buy Chinese memory, CXMT or YMTC, and does it work?

Every race produces synchronised video, control inputs and car state. Storage is exactly the thing that got expensive this year. Is your data a product, or a cost?

### F. Limits and close, 18 to 20

What can this not do yet that people assume it can?

What is the one thing that, if it broke on race day, would end the company?

Can you put the latency on the screen, live, while I drive a lap?

Short answers. Nvidia or Huawei: whose chips are in the box? If DRAM doubles again, what do you cut first? Your latency, in one word. One number everyone should remember from today.

### Held back

Someone on the internet wants to take over a car mid-race. How do you stop them?

DeepSeek proved China can do more with fewer chips. Is there a DeepSeek move in teleoperation: more with less bandwidth, cheaper hardware, smaller models?

## Narration, part 3

### Bridge to the broadcast lead

There are two kinds of video in this building. One has to arrive in milliseconds or the car crashes. The other can arrive seconds late and nobody minds. The first is engineering. The second is show business. Both have to work.

## Broadcast lead, 15 minutes

### A. Going live, 0 to 4

Walk me through the last sixty seconds before you go live. What are you looking at?

There are two kinds of video in this building: what the driver sees and what the audience sees. How different are they, and why?

### B. The craft, 4 to 9

Drone Racing League put the pilot's eyes on ESPN. You have the driver's eyes and the car's eyes at the same time.

How many cameras, which ones are on the car, and which single shot could you not broadcast a race without?

What does a viewer on Douyin see that a person in the venue never sees?

Do you show the latency number to the audience? Why, or why not?

What if you did? What would the comments say?

The best moment you have broadcast so far, and the one you wish you had not.

### C. The audience, 9 to 13

Formula 1 took seventy years and a Netflix series to find a new audience.

What is your Drive to Survive?

How do you make someone who does not play games care? Who is the main character of a race: the driver, the car or the engineer?

Same race, a viewer in Shanghai and a viewer in Stockholm. Do you produce one show or two? Commentary, language, pacing?

Peak concurrent viewers, average watch time, and the share who watched to the end.

### D. Close, 13 to 15

What could a Western studio do with your feed that you cannot do yourselves?

What moment are you still waiting to capture?

Short answers. Real car or simulator: which is harder to broadcast? One number everyone should remember from today.

### Held back

Which broadcast did you copy when you started, and where did you stop copying?

## Driver, 10 minutes

What does the delay feel like? Describe it in your body, not in numbers.

Where were you sitting when you lost the final? What was on the wall in front of you?

Your first crash in one of these: did you feel anything? What did you do in the next second?

You have raced in a game, with a handheld transmitter, and like this. Rank them by how hard they are, and by how real they feel.

What do you do differently on the last lap? Does the delay change how you brake?

How do you train for this? Is there anything you do that a sim racer would laugh at?

A sim racer in Europe thinks this would be easy for them. What would you tell them?

What do you tell your parents you do?

Short answers. Your latency, in one word. Motion seat: does it make you faster, or just happier? Who in the world would you most like to race?

## Narration, part 4

### Turn to robots

Then they showed me why the racing is only the beginning.

## Robot operator, 8 minutes

What are you controlling, from where, and how far away is it?

What is the hardest thing a robot does by remote: walking, picking something up, or turning around?

Has the robot ever done something you did not ask it to?

When the robot falls, what do you feel?

You have driven the race car too. Which is harder, and why?

Do you think of yourself as a gamer, a pilot, or a robot trainer?

Short answers. Five years from now, what gets driven remotely that nobody expects? One word for the delay.

## Narration, part 5

### Cross-border beat

Shanghai to Stockholm and back is about a hundred and sixty milliseconds on today's internet. Twice what they quote for the track. Nobody had tried to race across it. So we did.

### Closing

I came to Shanghai to see a race. What I found was a company using a sport to rehearse the next decade: humans, at a distance, driving machines that are not ready to drive themselves. The cars are the test. The robots are the business. And the clock, as always, is the only referee that cannot be argued with.

### Last line, to camera, dry

For the record: I crashed. The delay was [number] milliseconds. The excuse was mine.

## Words to watch

Stress is on the capital letters. Say each one ten times before you read the script.

- milliseconds: MIL-li-sec-onds
- kilometres: ki-LOM-e-tres (or KIL-o-me-tres; pick one and keep it)
- referee: ref-er-EE
- physics: FIZ-iks
- latency: LAY-ten-see
- synchronised: SIN-kro-nized
- teleoperation: tel-ee-op-er-AY-shun
- autonomous: aw-TON-o-mus
- humanoid: HYOO-ma-noid
- esports: EE-sports
- motorsport: MO-tor-sport
- commentating: COM-men-tay-ting
- sceptic: SKEP-tik
- novelty: NOV-el-tee
- Stockholm: STOCK-holm
- Einride: EYN-ride
- Ericsson: ER-ik-son
- Nvidia: en-VID-ee-a
- Huawei: HWAH-way
- SK Hynix: ess-kay HY-niks
- Abu Dhabi: AB-oo DAB-ee
- Douyin: DOH-yin
- Anting: AN-ting
- the T-box: TEE-box; the Ro-box: ROH-box
- DRAM: DEE-ram
- 5G-A: five-gee-AY

Rhythm rules. Pause at every comma. Land the last word of each sentence; do not let it fall away. Say numbers slowly: "eighty milliseconds", "a hundred and sixty". When a question has two parts, breathe between them. After every question, count one silent second before you move; the silence is where the answer comes from.
