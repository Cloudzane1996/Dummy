# Crypto Operational Security Checklist
_Last updated: 2025-06-05_

## Wallet Hygiene
- [ ] Generate seed phrases **offline** on a trusted device (air‑gapped if possible)
- [ ] Store seed on metal backup; split 2‑of‑3 locations
- [ ] Use hardware wallet (Ledger, Trezor, Keystone or similar) for > 1 000 USD value
- [ ] Verify address on device screen before signing

## Account Protection
- [ ] Separate email alias for each CEX / DeFi service
- [ ] 2‑Factor Auth via **TOTP hardware** (YubiKey/OnlyKey) – never SMS
- [ ] Unique, randomly‑generated passwords (≥ 16 chars) in password manager
- [ ] Revoke unused API keys quarterly

## Transaction Discipline
- [ ] Test send ≤ 10 USDT before large transfer
- [ ] Double‑confirm network (ERC‑20 vs BEP‑20 vs TRC‑20) fees & address
- [ ] Record TXID and store in portfolio tracker

## Phishing & Social
- [ ] Bookmark official domains; avoid search‑engine ads
- [ ] Never sign blind messages; decode on etherscan or Tenderly first
- [ ] Verify Telegram / Discord admins via cross‑channel mention

## Device Security
- [ ] Full‑disk encryption
- [ ] OS auto‑updates weekly; browser auto‑updates daily
- [ ] Disable browser extensions on wallet browser profile
- [ ] VPN on public Wi‑Fi
