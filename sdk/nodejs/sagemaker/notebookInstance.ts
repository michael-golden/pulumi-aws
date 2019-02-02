// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a Sagemaker Notebook Instance resource.
 * 
 * ## Example Usage
 * 
 * Basic usage:
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const aws_sagemaker_notebook_instance_ni = new aws.sagemaker.NotebookInstance("ni", {
 *     instanceType: "ml.t2.medium",
 *     name: "my-notebook-instance",
 *     roleArn: aws_iam_role_role.arn,
 *     tags: {
 *         Name: "foo",
 *     },
 * });
 * ```
 */
export class NotebookInstance extends pulumi.CustomResource {
    /**
     * Get an existing NotebookInstance resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NotebookInstanceState, opts?: pulumi.CustomResourceOptions): NotebookInstance {
        return new NotebookInstance(name, <any>state, { ...opts, id: id });
    }

    /**
     * The Amazon Resource Name (ARN) assigned by AWS to this notebook instance.
     */
    public /*out*/ readonly arn: pulumi.Output<string>;
    /**
     * The name of ML compute instance type.
     */
    public readonly instanceType: pulumi.Output<string>;
    /**
     * The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.
     */
    public readonly kmsKeyId: pulumi.Output<string | undefined>;
    /**
     * The name of the notebook instance (must be unique).
     */
    public readonly name: pulumi.Output<string>;
    /**
     * The ARN of the IAM role to be used by the notebook instance which allows SageMaker to call other services on your behalf.
     */
    public readonly roleArn: pulumi.Output<string>;
    /**
     * The associated security groups.
     */
    public readonly securityGroups: pulumi.Output<string[]>;
    /**
     * The VPC subnet ID.
     */
    public readonly subnetId: pulumi.Output<string | undefined>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags: pulumi.Output<{[key: string]: any} | undefined>;

    /**
     * Create a NotebookInstance resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NotebookInstanceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: NotebookInstanceArgs | NotebookInstanceState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: NotebookInstanceState = argsOrState as NotebookInstanceState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["instanceType"] = state ? state.instanceType : undefined;
            inputs["kmsKeyId"] = state ? state.kmsKeyId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["roleArn"] = state ? state.roleArn : undefined;
            inputs["securityGroups"] = state ? state.securityGroups : undefined;
            inputs["subnetId"] = state ? state.subnetId : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as NotebookInstanceArgs | undefined;
            if (!args || args.instanceType === undefined) {
                throw new Error("Missing required property 'instanceType'");
            }
            if (!args || args.roleArn === undefined) {
                throw new Error("Missing required property 'roleArn'");
            }
            inputs["instanceType"] = args ? args.instanceType : undefined;
            inputs["kmsKeyId"] = args ? args.kmsKeyId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["roleArn"] = args ? args.roleArn : undefined;
            inputs["securityGroups"] = args ? args.securityGroups : undefined;
            inputs["subnetId"] = args ? args.subnetId : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
        }
        super("aws:sagemaker/notebookInstance:NotebookInstance", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering NotebookInstance resources.
 */
export interface NotebookInstanceState {
    /**
     * The Amazon Resource Name (ARN) assigned by AWS to this notebook instance.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The name of ML compute instance type.
     */
    readonly instanceType?: pulumi.Input<string>;
    /**
     * The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.
     */
    readonly kmsKeyId?: pulumi.Input<string>;
    /**
     * The name of the notebook instance (must be unique).
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ARN of the IAM role to be used by the notebook instance which allows SageMaker to call other services on your behalf.
     */
    readonly roleArn?: pulumi.Input<string>;
    /**
     * The associated security groups.
     */
    readonly securityGroups?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The VPC subnet ID.
     */
    readonly subnetId?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}

/**
 * The set of arguments for constructing a NotebookInstance resource.
 */
export interface NotebookInstanceArgs {
    /**
     * The name of ML compute instance type.
     */
    readonly instanceType: pulumi.Input<string>;
    /**
     * The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt the model artifacts at rest using Amazon S3 server-side encryption.
     */
    readonly kmsKeyId?: pulumi.Input<string>;
    /**
     * The name of the notebook instance (must be unique).
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ARN of the IAM role to be used by the notebook instance which allows SageMaker to call other services on your behalf.
     */
    readonly roleArn: pulumi.Input<string>;
    /**
     * The associated security groups.
     */
    readonly securityGroups?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The VPC subnet ID.
     */
    readonly subnetId?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
}
