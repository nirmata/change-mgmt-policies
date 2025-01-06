## Scanning CloudFormation templates for misconfigurations

This is a demo repository to scan the [CloudFormation]([url](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)) templates. The scanned results can be viewed via the [Nirmata Policy Manager (NPM)]([url](https://nirmata.com/policy-manager/)).

The GitHub Action converts the CDK file into a CloudFormation template using the `cdk synth` command.
```
- name: CDK Synth
  run: |
    cd sample-cdk
    cdk synth --json
```

In the next step, the policies are applied on the generated JSON file. The results are then published to NPM.
```
- name: NCTL Scan Repository for CDK
  run: |
    nctl scan json -r sample-cdk/cdk.out/MyEcsStack.template.json --policies policies/ --publish
```

![image](https://github.com/user-attachments/assets/2be97d3a-3833-4a42-971c-062b3e992108)

