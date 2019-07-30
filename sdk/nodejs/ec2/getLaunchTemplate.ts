// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides information about a Launch Template.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const defaultLaunchTemplate = pulumi.output(aws.ec2.getLaunchTemplate({
 *     name: "my-launch-template",
 * }));
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/launch_template.html.markdown.
 */
export function getLaunchTemplate(args: GetLaunchTemplateArgs, opts?: pulumi.InvokeOptions): Promise<GetLaunchTemplateResult> & GetLaunchTemplateResult {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetLaunchTemplateResult> = pulumi.runtime.invoke("aws:ec2/getLaunchTemplate:getLaunchTemplate", {
        "name": args.name,
        "tags": args.tags,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getLaunchTemplate.
 */
export interface GetLaunchTemplateArgs {
    /**
     * The name of the launch template.
     */
    readonly name: string;
    readonly tags?: {[key: string]: any};
}

/**
 * A collection of values returned by getLaunchTemplate.
 */
export interface GetLaunchTemplateResult {
    /**
     * Amazon Resource Name (ARN) of the launch template.
     */
    readonly arn: string;
    /**
     * Specify volumes to attach to the instance besides the volumes specified by the AMI.
     */
    readonly blockDeviceMappings: { deviceName: string, ebs: { deleteOnTermination: string, encrypted: string, iops: number, kmsKeyId: string, snapshotId: string, volumeSize: number, volumeType: string }[], noDevice: string, virtualName: string }[];
    /**
     * Customize the credit specification of the instance. See Credit
     * Specification below for more details.
     */
    readonly creditSpecifications: { cpuCredits: string }[];
    /**
     * The default version of the launch template.
     */
    readonly defaultVersion: number;
    /**
     * Description of the launch template.
     */
    readonly description: string;
    /**
     * If `true`, enables [EC2 Instance
     * Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)
     */
    readonly disableApiTermination: boolean;
    /**
     * If `true`, the launched EC2 instance will be EBS-optimized.
     */
    readonly ebsOptimized: string;
    /**
     * The elastic GPU to attach to the instance. See Elastic GPU
     * below for more details.
     */
    readonly elasticGpuSpecifications: { type: string }[];
    /**
     * The IAM Instance Profile to launch the instance with. See Instance Profile
     * below for more details.
     */
    readonly iamInstanceProfiles: { arn: string, name: string }[];
    /**
     * The AMI from which to launch the instance.
     */
    readonly imageId: string;
    /**
     * Shutdown behavior for the instance. Can be `stop` or `terminate`.
     * (Default: `stop`).
     */
    readonly instanceInitiatedShutdownBehavior: string;
    /**
     * The market (purchasing) option for the instance.
     * below for details.
     */
    readonly instanceMarketOptions: { marketType: string, spotOptions: { blockDurationMinutes: number, instanceInterruptionBehavior: string, maxPrice: string, spotInstanceType: string, validUntil: string }[] }[];
    /**
     * The type of the instance.
     */
    readonly instanceType: string;
    /**
     * The kernel ID.
     */
    readonly kernelId: string;
    /**
     * The key name to use for the instance.
     */
    readonly keyName: string;
    /**
     * The latest version of the launch template.
     */
    readonly latestVersion: number;
    /**
     * The monitoring option for the instance.
     */
    readonly monitorings: { enabled: boolean }[];
    readonly name: string;
    /**
     * Customize network interfaces to be attached at instance boot time. See Network
     * Interfaces below for more details.
     */
    readonly networkInterfaces: { associatePublicIpAddress: boolean, deleteOnTermination: boolean, description: string, deviceIndex: number, ipv4AddressCount: number, ipv4Addresses: string[], ipv6AddressCount: number, ipv6Addresses: string[], networkInterfaceId: string, privateIpAddress: string, securityGroups: string[], subnetId: string }[];
    /**
     * The placement of the instance.
     */
    readonly placements: { affinity: string, availabilityZone: string, groupName: string, hostId: string, spreadDomain: string, tenancy: string }[];
    /**
     * The ID of the RAM disk.
     */
    readonly ramDiskId: string;
    /**
     * A list of security group names to associate with. If you are creating Instances in a VPC, use
     * `vpc_security_group_ids` instead.
     */
    readonly securityGroupNames: string[];
    /**
     * The tags to apply to the resources during launch.
     */
    readonly tagSpecifications: { resourceType: string, tags: {[key: string]: any} }[];
    /**
     * (Optional) A mapping of tags to assign to the launch template.
     */
    readonly tags: {[key: string]: any};
    /**
     * The Base64-encoded user data to provide when launching the instance.
     */
    readonly userData: string;
    /**
     * A list of security group IDs to associate with.
     */
    readonly vpcSecurityGroupIds: string[];
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
