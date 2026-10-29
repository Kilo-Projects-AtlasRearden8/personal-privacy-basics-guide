# Locking down your accounts

Your accounts — email, banking, shopping, social media — are the front doors to your digital life. This chapter walks you through locking them down, step by step. You do not need to be technical. You just need about an hour and a willingness to click through some settings.

Every name, email, phone number, and address in this guide is made up. Do not copy them as if they were real, and never type your own real details into examples.

## Step 1: Use strong, unique passwords

A strong password is long and hard to guess. A unique password means you use a different one for every account.

Why it matters: if one company gets hacked and your password leaks, attackers try that same password on your other accounts. If you reuse passwords, one break-in becomes many.

### How to do it

1. **Get a password manager.** This is an app that remembers your passwords for you. You only need to remember one strong "master password" to unlock it. Examples: Bitwarden, 1Password, Apple Passwords (iCloud Keychain), Google Password Manager.
2. **Let the password manager create passwords.** When you make or change an account, have the manager suggest a long random password (16+ characters). You do not need to memorize it.
3. **Save the password** in the manager before you finish creating the account.
4. **Change your most important passwords first:** email, banking, password manager itself, phone accounts (Apple/Google), and anything with payment info stored.

### Example (fake)

Instead of reusing `Spring2024!` everywhere, your password manager might create:

- Email: `kP9#mV2&xQ7!wL5r`
- Bank: `zR4@bN8!tY3*hW6j`
- Shopping: `mC2$fG7^pD5!vK9n`

You never see most of these again — the manager fills them in for you.

### Master password tips

- Make it long: four or five random words strung together works well (for example: `purple-train-socks-library-planet`). Do not use that exact phrase — make up your own.
- Do not store the master password in the password manager. Write it down on paper and keep it somewhere safe at home, or memorize it.
- Never share your master password with anyone, including people claiming to be "tech support."

## Step 2: Turn on two-factor authentication (2FA)

2FA means that even if someone steals your password, they still cannot get into your account without a second piece of proof — usually a code from your phone.

### How to do it

1. Go to Settings → Security (or "Sign-in & security") in each account.
2. Look for "Two-factor authentication," "Two-step verification," or "MFA."
3. Choose **authenticator app** as the method if offered (Google Authenticator, Microsoft Authenticator, Authy, or your password manager's built-in authenticator).
4. Scan the QR code with the app, then type in the six-digit code it shows to finish setup.
5. Save the **backup codes** the site gives you. Print them or write them down and keep them with your master password. These let you in if you lose your phone.

### Authenticator app vs. text message (SMS)

Authenticator apps are safer than SMS codes. Attackers can sometimes hijack your phone number and receive your texts. Use an app when you can; SMS is still better than nothing.

### Example setup (fake)

- Service: `examplebank.example`
- You open: Settings → Security → Two-factor authentication → Authenticator app
- You scan a QR code with your authenticator app
- The app shows: `482 917`
- You type `482917` on the website → 2FA is on

## Step 3: Lock down your email account first

Your email is the master key. If someone gets into your email, they can request password resets for almost everything else.

1. Put a strong, unique password on your email.
2. Turn on 2FA (authenticator app).
3. Check the recovery email and phone number listed on the account. Make sure they belong to you and are current.
4. Remove any old phone numbers or email addresses you no longer control.
5. Turn on login alerts if the service offers them (you get notified when someone signs in from a new device).

## Step 4: Review what is connected to your accounts

Many accounts let you see which devices are signed in and which apps have access.

### How to do it

1. In each important account, find "Devices," "Where you're signed in," or "Active sessions."
2. Sign out of any device you do not recognize or no longer use (old phones, old laptops, a friend's computer you borrowed once).
3. Find "Connected apps," "Third-party access," or "Apps with access to your account."
4. Remove access for apps and services you no longer use. That quiz website from 2016 probably does not still need access to your contacts.

## Step 5: Check privacy settings on social media

1. Set your profile to "private" or "friends only" if you do not need to be public.
2. Limit who can see your friends list, birthday, phone number, and email address.
3. Turn off settings that let people find you by your email or phone number, unless you want that.
4. Review past posts and delete anything that shares too much (your address, vacation plans, photos of your ID or credit card).

## Step 6: Know if your data has been in a breach

1. Use a free breach-check service (for example, haveibeenpwned.com) with your email address.
2. If a breach shows up for an account you still use, change that password right away — and any other account where you reused it.
3. If the breach involved payment info, watch your bank and card statements closely for charges you did not make.

### What these services do (simple version)

You type in your email. The service checks whether that email appeared in any known data breaches and tells you which ones. It does not reveal your password.

## Step 7: Security questions are not secure

Many sites ask "What was your first pet's name?" These answers are often guessable or findable online.

### Better approach

- Treat security questions like passwords: make up answers and save them in your password manager.
- Example (fake): Q: "First pet's name?" A: `Refrigerator-Blue-42`. Save that in your password manager next to the account.
- Do not use real answers like your mother's actual maiden name or your actual first school.

## Quick checklist for this chapter

- [ ] Password manager installed
- [ ] Strong, unique password on email, banking, and password manager
- [ ] 2FA turned on (authenticator app preferred) for email and banking
- [ ] Backup codes saved
- [ ] Old devices signed out
- [ ] Unused connected apps removed
- [ ] Social media set to private / limited
- [ ] Breach check run for your email
- [ ] Security question answers made up and saved

You do not have to do all of this today. Pick one account and start there.
