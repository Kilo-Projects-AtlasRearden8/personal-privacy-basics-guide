# Opting out of AI training

Many AI companies use what people type into their AI tools to train future versions of their models. That means your conversations could be read by human reviewers, stored for a long time, or used to teach the AI to write like you.

This chapter shows you how to turn that off in popular AI tools. It does not delete past conversations — it mostly stops future ones from being used for training.

Every account name and email in this guide is made up.

## Step 1: ChatGPT (OpenAI)

### On the web
1. Log in to chatgpt.example (use the real site you normally use; `example` addresses here are placeholders).
2. Click your profile → Settings → Data controls.
3. Turn off **"Improve the model for everyone."** (In some versions this is called "Chat history & training" — turn it off.)
4. With this off, your conversations are not used to train OpenAI's models.

### On iPhone/Android
1. Open the ChatGPT app → profile icon → Settings → Data controls.
2. Turn off "Improve the model for everyone."

### Delete your data
1. Settings → Data controls → Clear chat history (or Manage → Delete).
2. You can also request deletion of your account data through OpenAI's privacy portal.

Note: Even with training off, OpenAI keeps conversations for about 30 days for abuse monitoring, then deletes them.

## Step 2: Claude (Anthropic)

1. Log in to claude.example.
2. Click your profile → Settings.
3. Turn off **"Train on my content"** (or uncheck "Allow Claude to use your conversations for training").
4. Free accounts: conversations may be reviewed by human contractors for safety. Paid (Pro/Team/Enterprise) accounts are opted out of training by default — check your settings to confirm.

## Step 3: Gemini (Google)

1. Log in to gemini.example.
2. Select Activity → Turn off Gemini Apps Activity, or set it to auto-delete after 3 or 36 months.
3. In Settings, look for "Train on my content" or similar and turn it off.
4. Your Google account settings (myaccount.google.com → Data & privacy) also control whether Google uses your data for AI improvements.

## Step 4: Microsoft Copilot

1. Log in to copilot.microsoft.com with your Microsoft account.
2. Go to Settings → Privacy.
3. Turn off options that let Microsoft use your chat data to train models.
4. If you use Copilot with a work or school account (Microsoft 365), your organization may already have data protection turned on — ask your IT admin if unsure.

## Step 5: Meta AI (Facebook, Instagram, Messenger, WhatsApp)

Meta may use posts and messages to train AI. Options vary by country (for example, EU/UK users have stronger opt-out rights under GDPR).

1. In Facebook or Instagram: Settings → Privacy → Meta AI (or "AI at Meta").
2. Look for an option to object to your data being used for AI training and submit it.
3. In WhatsApp: Settings → Privacy → Chats — avoid sending sensitive info to the Meta AI button; there is no full training opt-out in all regions yet.

## Step 6: Other AI tools (writing assistants, image generators, code tools)

For any AI tool you use:
1. Look in Settings → Privacy or Settings → Data.
2. Search "[tool name] opt out of AI training" to find the company's instructions.
3. If you cannot find an opt-out, assume your input may be used for training — do not type in passwords, financial details, health info, or other people's private data.

## Step 7: Local AI (runs on your own computer)

If you want AI that never sends your data to a company, run models locally on your own machine. Examples: Ollama, LM Studio, Jan, or llama.cpp. These run offline after you download the model, and nothing leaves your computer. This chapter series does not cover setup in detail, but local AI is the most private option.

## What opting out does and does not do

| Does | Does not |
|------|----------|
| Stops future conversations from being used to train the model (in most tools) | Delete conversations you already had (you must delete those separately) |
| Reduce how much human reviewers can see | Guarantee the company never sees anything (abuse monitoring may still keep data briefly) |
| Apply to the account you changed | Apply to other accounts or other people's chats with you |

## Quick checklist for this chapter

- [ ] ChatGPT: "Improve the model for everyone" turned off
- [ ] Claude: "Train on my content" turned off
- [ ] Gemini: Gemini Apps Activity turned off or set to auto-delete
- [ ] Copilot: training use turned off (check with IT for work accounts)
- [ ] Meta AI: objection/opt-out submitted (where available)
- [ ] Other AI tools: privacy settings reviewed
- [ ] Rule adopted: never paste passwords, financial data, health details, or others' private info into AI tools
